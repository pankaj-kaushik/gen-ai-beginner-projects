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
- ⚠️ Never commit .env to GitHub.

## ▶️ How to Run the Project
### Step 1: Update ```input.txt``` File
Copy and past content of your blog post or article in input.txt file
### Step 2: Run main.py
```bash
python main.py
```
## 🧠 Prompt Used
```text
You are a professional editor. Summarize the following text in simple language.\nUse 4-5 bullet points.\nMake it easy for beginners to understand.
```

## 📌 Sample Output
--- Welcome to your Text Summarizer Writer! ---
Loading environment variables...
Reading input text from file...
Creating prompt...
You are a professional editor. Summarize the following text in simple language.
Use 4-5 bullet points.
Make it easy for beginners to understand.
Artificial Intelligence (AI) has revolutionized modern technology and society. AI refers to computer systems designed to perform tasks that typically 
require human intelligence, such as learning, reasoning, and problem-solving.
Machine learning, a subset of AI, enables systems to learn from data without explicit programming. Deep learning uses neural networks to process complex patterns, powering applications like image recognition and natural language processing.
AI applications are widespread across industries. In healthcare, AI assists in disease diagnosis and drug discovery. Finance uses AI for fraud detection and algorithmic trading. Autonomous vehicles rely on AI for navigation and decision-making.
Natural language processing allows computers to understand and generate human language, enabling chatbots and virtual assistants like voice recognition systems.
However, AI development raises ethical concerns. Issues include data privacy, algorithmic bias, job displacement, and autonomous weapon systems. Responsible AI development requires transparency, fairness, and accountability.
The future of AI is promising yet uncertain. Advances in quantum computing and neuromorphic chips will enhance AI capabilities. Researchers focus on creating explainable AI and ensuring human oversight.
AI literacy is becoming essential as the technology permeates society. Understanding AI's capabilities and limitations helps individuals make informed decisions about its implementation and regulation, shaping a beneficial technological future.
Creating Gen AI client...
Generating summary...
Summary: Here is a simple summary of the text:

*   **What it is:** Artificial Intelligence (AI) is technology that allows computers to do things that usually require human intelligence, such as learning, reasoning, and solving problems.
*   **How we use it:** AI is already all around us. it helps doctors diagnose diseases, allows cars to drive themselves, and powers digital assistants that can understand and talk to humans.
*   **The risks:** Despite its benefits, AI raises concerns about privacy, fairness, and the possibility of computers taking over human jobs. It is important to build AI that is transparent and treats everyone fairly.
*   **The future:** As technology improves, researchers are working to make AI more powerful while ensuring that humans stay in control and can understand how the AI makes its decisions.
*   **Why it matters:** Because AI is becoming a part of everyday life, it is important for everyone to learn the basics. This helps us use the technology wisely and make good decisions about its role in our future.

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