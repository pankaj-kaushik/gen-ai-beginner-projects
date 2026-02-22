# 📘 AI Text Similarity Checker Using Gemini And Python

## 📌 Introduction
Welcome to the **AI Text Similarity Checker** project! 🤖✨  

This beginner-friendly Generative AI project demonstrates how to build a **semantic search system** using:

- 🧠 Text embeddings  
- 📐 Cosine similarity  
- 🗂️ Vector indexing  
- ⚡ Top-K nearest neighbor search  

We use **Python** and embeddings from **Google Gemini** to convert sentences into high-dimensional vectors and find the most semantically similar sentence to a user query.

> ⚠️ This project does NOT use RAG (Retrieval-Augmented Generation).  
It focuses purely on **embedding-based similarity search**.

## 🚀 What This Project Does
- Stores multiple sentences in memory (vector store)
- Converts each sentence into embeddings using Gemini
- Converts the user query into an embedding
- Calculate similarity between query and stored sentences
- Returns the most semantically similar sentences

## 🎯 Learning Outcomes
After completing this project, you will understand:
- 🧬 How text embeddings works
- ✨ How to generate embeddings using Gemini
- 📏 How cosine similarity measures semantic closeness
- 🗃️ How vector indexing works
- 🏗️ Core foundation behind modern AI search systems

This project builds strong fundamentals before moving to:

- 🔥 RAG systems  
- 🤖 AI chatbots  
- 📚 Knowledge retrieval systems  
- 🧠 AI agents  

## 🏢 Industry Use Cases
This semantic similarity system can be applied in real-world industries:

### 💬 1. Duplicate Question Detection
- Identify repeated questions in forums
- Prevent redundant support tickets

### 📚 2. FAQ Matching Systems
- Match user queries to closest FAQ answers
- Automate customer support

### 🔎 3. Semantic Search Engines
- Search meaning, not keywords
- Improve knowledge base search accuracy

### 🛍️ 4. E-commerce Search
- Match “cheap phone” with “budget smartphone”

### 🧾 5. Document Similarity Detection
- Identify similar contracts or reports
- Content plagiarism detection

## 🧩 Architecture & Sequence Flow
```text
User -> CLI Interface -> Input Collection (Query Sentence) -> Gemini Embedding API -> Embedding Generation -> Cosine Similarity Calculation -> Top-K Similarity Search -> Result Display
```
**Detailed Flow:**

1. Application starts - Welcome message and instructions displayed
2. User input collection - Prompt user for a query sentence
3. Embedding generation - Gemini API converts stored sentences and query into embeddings
4. Similarity calculation - Compute cosine similarity between query embedding and stored embeddings
5. Top-K search - Identify the most semantically similar sentences (Top-K)
6. Output display - Show the closest matching sentences to the user
7. Error handling - Manage API errors, empty input, and invalid responses gracefully

## ▶️ How to Run the Project
### Run Application
```bash
python ai-text-similarity-checker.py
```
## 📌 Sample Output
```powershell
--- Welcome to AI Text Similarity Checker! ---
Generating embeddings for sample sentences...

Embeddings generated for 5 sentences.

------------------------------------------------------------
Setting up ChromaDB collection and adding documents...

Documents added to ChromaDB collection.

Enter a sentence to check for similarity: what is python

Top 3 similar sentences:
1. Python is a popular programming language.
2. Artificial intelligence is transforming the world.
------------------------------------------------------------
```

## ✨ Future Enhancements
### 🌍 Multi-Language Similarity
Enable cross-language matching (English ↔ Hindi ↔ Spanish).

### 📄 Real-Time Document Ingestion
- Upload PDFs
- Auto-split into chunks
- Generate embeddings dynamically

### 🧠 Automatic Clustering
Group similar content using K-Means clustering.

### 🗄️ Production-Ready Vector Database
Integrate:
- FAISS (local)
- Pinecone (cloud)
- Weaviate
- Chroma

### 🌐 Build a Web App
Deploy using:
- Streamlit
- FastAPI
- Flask

### 🐛 Troubleshooting
Common Issues:
**API Key Error:**
```python
Error: GEMINI_API_KEY not found
Solution: Create a `.env` file in the project directory with:
GEMINI_API_KEY=your_key_here
```

**Connection Error:**
```python
Error: Failed to connect to Gemini API
Solution: Check your internet connection and verify Gemini API service is operational.
```

**Timeout Error:**
```python
Error: Request timed out
Solution: Try again later or check Gemini API status. Increase timeout in code if needed.
```

**Invalid Input Error:**
```python
Error: Empty input or invalid sentence
Solution: Enter a non-empty sentence for similarity checking.
```

**Embedding Generation Error:**
```python
Error: Failed to generate embeddings
Solution: Ensure your API key is valid and Gemini API is accessible.
```

**ChromaDB Error:**
```python
Error: Failed to add documents to ChromaDB
Solution: Check ChromaDB installation and ensure dependencies are installed.
```
```

## Contributing
💡 If you found this helpful...
- ⭐ Star the repo
- 🍴 Fork it
- 🚀 Build on top of it & submit pull request
- 📢 Share your learning journey with the community

## 🙌 Acknowledgements
- Google Gemini LLM
- Open-source Python community
- All learners and educators using this tool

---
Happy Searching! 🤖🔍  
**Discover the power of AI-driven text similarity—find meaningful connections, faster and smarter!**
