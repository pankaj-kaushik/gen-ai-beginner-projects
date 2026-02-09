"""
Study Buddy - An AI-Powered Learning Assistant

This module provides an interactive learning experience using Google's Gemini API.
It helps users understand complex concepts through simple explanations, analogies,
key takeaways, and quiz questions.

Usage:
    python main.py
    
Requirements:
    - google-genai library
    - python-dotenv library
    - GEMINI_API_KEY environment variable
"""

import os
from dotenv import load_dotenv
from google import genai


def create_genai_client():
    """
    Initializes and returns a Google GenAI client.
    
    The client automatically uses the GEMINI_API_KEY from the environment
    to authenticate with Google's API.
    
    Returns:
        genai.Client: An authenticated GenAI client instance.
    """
    print("Creating Gen AI client...")
    return genai.Client()

def create_prompt(topic):
    """
    Constructs a structured prompt for the Gemini model.
    
    This function creates a detailed system-style prompt that instructs Gemini
    to act as a Study Buddy and provide explanations in a specific format.
    
    Args:
        topic (str): The concept or topic the user wants to learn about.
        
    Returns:
        str: A formatted prompt string with instructions for the AI model.
    """
    # We use a system-style prompt to guide Gemini's behavior
    prompt = f"""
    You are an expert Study Buddy. 
    1. Explain the concept of '{topic}' in simple terms (suitable for a 10-year-old).
    2. Use an analogy to make it memorable.
    3. Provide 3 bullet points of key takeaways.
    4. Generate 2 multiple-choice questions to test the user's understanding.
    """
    return prompt

def initialize_environment():
    """
    Initializes the application environment.
    
    This function:
    1. Loads environment variables from a .env file using python-dotenv
    2. Verifies that the GEMINI_API_KEY is available
    3. Prints the API key status for debugging purposes
    
    Note: In production, sensitive information like API keys should not be printed.
    """
    # Initialize environment variables
    print("Loading environment variables...")
    load_dotenv()

    # The client gets the API key from the environment variable `GEMINI_API_KEY`.
    # print("API KEY:", os.getenv("GEMINI_API_KEY"))

def explain_concept(client, prompt):
    """
    Generates a simple explanation and quiz for a given topic using Gemini.
    
    This function calls the Gemini API with the provided prompt and returns
    the model's response. It includes error handling for API failures.
    
    Args:
        client (genai.Client): An authenticated GenAI client instance.
        prompt (str): The formatted prompt containing the topic and instructions.
        
    Returns:
        str: The AI-generated explanation, analogies, key points, and quiz questions.
             If an error occurs, returns an error message string.
    """
    try:
        response = client.models.generate_content(
            model="gemini-3-flash-preview",  # Using the fast and capable flash model
            contents=prompt
        )
        return response.text
    except Exception as e:
        return f"An error occurred: {e}"

def main():
    """
    Main entry point for the Study Buddy application.
    
    This function orchestrates the learning flow:
    1. Displays a welcome message
    2. Initializes the environment and API client
    3. Prompts the user for a topic to learn about
    4. Generates a customized explanation with analogies and quiz questions
    5. Displays the results in a formatted manner
    """
    print("--- Welcome to your AI Study Buddy! ---")
    initialize_environment()
    topic = input("What concept would you like to learn today? ")
    print(f"\nAnalyzing '{topic}'... Please wait.\n")
    print("Creating prompt...")
    user_prompt = create_prompt(topic)
    client = create_genai_client()
    explanation = explain_concept(client, user_prompt)
    print("-" * 30)
    print(explanation)
    print("-" * 30)

if __name__ == "__main__":
    main()