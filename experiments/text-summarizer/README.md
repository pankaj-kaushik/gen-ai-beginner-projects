# 🧠 AI Text Summarizer (Using Gemini LLM)

A beginner-friendly **GenAI project built with Python** that summarizes long text into short, easy-to-understand bullet points using **Google Gemini Large Language Model**.

This project is ideal for:
- Students 📚
- Working professionals 👨‍💻
- Content creators ✍️
- Anyone who wants quick insights from long articles

## 🚀 What This Project Does
- Takes **long text input** from the user
- Sends it to **Gemini LLM**
- Returns a **concise summary** in simple language
- Uses **bullet points** for better readability

## 🧩 Use Cases
- Summarizing blog posts or articles  
- Making quick notes from study material  
- Understanding long documentation faster  
- Preparing revision notes  

## ⚙️ Setup Instructions
### Step 1: Clone the Repository
```bash
git clone https://github.com/pankaj-kaushik/genai-labs.git
cd text-summarizer
```
### Step 2: Create Virtual Environment
```bash
python -m venv .venv
```
Activate it:

**Windows (PowerShell):**
```bash
.venv\Scripts\Activate.ps1
```

**Mac/Linux:**
```bash
source .venv/bin/activate
```
### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```
### Step 4: Get Gemini API Key
- Visit Google AI Studio (https://aistudio.google.com/api-keys)
- Create a new API Key
- Copy the key

### Step 5: Create .env File
- Create a file named ```.env``` in the root directory and update the Gemini API Key
- Note: You can use ```.env.example``` file and rename it to ```.env```

## ▶️ How to Run the Project
### Step 1: Update ```input.txt``` File
Copy and past content of your blog post or article in input.txt file
### Step 2: Run main.py
```bash
python main.py
```

## 📌 Sample Output
- Explains the main idea clearly  
- Highlights key points only  
- Removes unnecessary details  
- Easy to understand for beginners  

## ✨ Future Enhancements
- Add Streamlit web UI
- Support PDF / text file input
- Choose summary length (short / medium / detailed)
- Language selection (English / Hindi)
- Save summaries to file

## 🎯 Learning Outcomes
- How GenAI APIs work
- Prompt engineering basics
- Secure API key handling
- Real-world GenAI use cases
- End-to-end AI application flow

## Contributing
Feel free to fork this repo, improve it, and submit a pull request 🚀

## 🙌 Acknowledgements
- Google Gemini LLM
- Open-source Python community