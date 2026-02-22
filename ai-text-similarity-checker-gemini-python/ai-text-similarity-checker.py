"""
AI Text Similarity Checker

This module implements a text similarity checker using Google's Gemini embedding model
and ChromaDB for vector storage. It allows users to compare a query sentence against
a collection of predefined sentences and find the most similar matches.

The application:
1. Generates embeddings for a set of sample sentences using Gemini API
2. Stores the embeddings in a ChromaDB collection
3. Accepts user input and finds the top 3 most similar sentences

Requirements:
    - GEMINI_API_KEY environment variable must be set (via .env file)
    - chromadb, python-dotenv, and google-genai packages installed

Author: Generated with AI assistance
Date: February 2026
"""

import os
import chromadb
from dotenv import load_dotenv
from google import genai

# Load environment variables from .env file
load_dotenv()

# Constants
TARGET_MODEL = "gemini-embedding-001"  # Gemini embedding model for semantic similarity
SENTENCES = [
    "The cat sat on the mat.",
    "A quick brown fox jumps over the lazy dog.",
    "Artificial intelligence is transforming the world.",
    "OpenAI develops advanced AI models.",
    "Python is a popular programming language."
]

def create_genai_client() -> 'genai.Client':
    """Initialize and return an authenticated GenAI client.

    The client uses the `GEMINI_API_KEY` from the environment (or `.env`).

    Returns:
        genai.Client: Authenticated GenAI client instance.
    """
    return genai.Client()

def create_chromadb_client() -> 'chromadb.Client':
    """Initialize and return a ChromaDB client.

    Returns:
        chromadb.Client: An instance of the ChromaDB client.
    """
    return chromadb.Client()

def create_collection(chromadb_client: 'chromadb.Client', name: str) -> 'chromadb.Collection':
    """Create and return a ChromaDB collection with the specified name.

    Args:
        chromadb_client: An instance of the ChromaDB client.
        name: The name of the collection to create.

    Returns:
        chromadb.Collection: The created collection instance.
    """
    return chromadb_client.create_collection(name=name, configuration={"hnsw": {"space": "cosine"}})

def add_documents_to_collection(collection: 'chromadb.Collection', documents: list[str], embeddings: list[list[float]], ids: list[str]) -> None:
    """Add documents along with their embeddings and IDs to the specified ChromaDB collection.

    Args:
        collection: The ChromaDB collection to which the documents will be added.
        documents: A list of text documents to be stored in the collection.
        embeddings: A list of lists of floats representing the embeddings for each document.
        ids: A list of unique identifiers corresponding to each document.

    Returns:
        None
    """
    collection.add(documents=documents, embeddings=embeddings, ids=ids)

def create_ids():
    """Generate unique IDs for each sentence in the SENTENCES list.
    
    Creates sequential IDs in the format 'id0', 'id1', etc. to uniquely
    identify each document in the ChromaDB collection.
    
    Returns:
        list[str]: A list of unique string identifiers.
    """
    return [f"id{i}" for i in range(len(SENTENCES))]
    
def get_embeddings(client: 'genai.Client', text: list[str]):
    """Generate and return embeddings for the given text using the GenAI API.
    
    Uses the Gemini embedding model to convert text into numerical vector
    representations that capture semantic meaning. These embeddings can be
    used for similarity comparison.

    Args:
        client (genai.Client): Authenticated GenAI client instance.
        text (list[str]): List of input text strings to be converted into embeddings.
        
    Returns:
        list[list[float]]: A list of embedding vectors, where each vector is a list
                          of floats. Returns an empty list if an error occurs.
                          
    Raises:
        Prints error message if embedding generation fails.
    """
    try:
        response = client.models.embed_content(
            model=TARGET_MODEL,
            contents=text,
            config=genai.types.EmbedContentConfig(task_type="SEMANTIC_SIMILARITY")
        )
        return [e.values for e in response.embeddings]
    except Exception as e:
        print(f"An error occurred while generating embeddings: {e}")
        return []

def find_similar_sentences(collection: 'chromadb.Collection', query_embedding: list[float], n_results: int = 2) -> list[str]:
    """Find and return the most similar sentences from the ChromaDB collection based on the query embedding.
    
    This function performs a similarity search using the provided query embedding against the
    embeddings stored in the specified ChromaDB collection. It retrieves the top N most similar
    sentences based on cosine similarity.

    Args:
        collection (chromadb.Collection): The ChromaDB collection to search within.
        query_embedding (list[float]): The embedding vector for the user's query sentence.
        n_results (int): The number of top similar sentences to retrieve (default is 3).
        
    Returns:
        list[str]: A list of the most similar sentences retrieved from the collection.
    """
    results = collection.query(query_embeddings=query_embedding, n_results=n_results)
    return results['documents'][0]

def main() -> None:
    """Main function to run the AI Text Similarity Checker application.
    
    This function orchestrates the entire workflow:
    1. Initializes the GenAI client and generates embeddings for sample sentences
    2. Sets up ChromaDB and stores the embeddings
    3. Prompts the user for input and finds similar sentences
    4. Displays the top 3 most similar results
    
    Returns:
        None
    """
    print("--- Welcome to AI Text Similarity Checker! ---")
    print("Generating embeddings for sample sentences...\n")
    
    # Initialize GenAI client and generate embeddings for sample sentences
    genai_client = create_genai_client()
    embeddings = get_embeddings(genai_client, SENTENCES)
    print(f"Embeddings generated for {len(SENTENCES)} sentences.\n")
    print("-" * 60)
    
    # Set up ChromaDB collection and add documents with their embeddings
    print("Setting up ChromaDB collection and adding documents...\n")
    chromadb_client = create_chromadb_client()
    collection = create_collection(chromadb_client, "text_similarity_collection")
    add_documents_to_collection(collection, SENTENCES, embeddings, create_ids())
    print("Documents added to ChromaDB collection.\n")
    
    # Get user input and perform similarity search
    user_query = input("Enter a sentence to check for similarity: ")
    query_embedding = get_embeddings(genai_client, [user_query])
    
    # Display results if embeddings were successfully generated
    if query_embedding:
        # Perform cosine similarity search (ChromaDB's default distance metric)
        # to find the 3 most similar documents to the query embedding
        #results = collection.query(query_embeddings=query_embedding, n_results=3)
        results = find_similar_sentences(collection, query_embedding)
        print("\nTop 2 similar sentences:")
        for idx, doc in enumerate(results):
            print(f"{idx + 1}. {doc}")
    print("-" * 60)
    

if __name__ == "__main__":
    main()