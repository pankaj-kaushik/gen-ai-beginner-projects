# 📘 AI Study Buddy / Concept Explainer (Gemini LLM)

An AI-powered **Study Buddy** built using **Python** and **Google Gemini LLM** that explains complex concepts in **simple, beginner-friendly language** using real-life analogies and examples.

This project helps learners quickly understand difficult topics without technical jargon.

This project is ideal for:
- Students 📚
- Working professionals 👨‍💻
- Content creators ✍️
- Anyone who wants quick insights from long articles

## 🚀 What This Project Does
- Enter any topic or concept
- Get simplified explanations
- Understand using real-life analogies
- Learn faster with beginner-friendly examples

## 🧩 Use Cases
✅ Students learning new subjects  
✅ Software engineers learning new technologies  
✅ Interview preparation  
✅ Quick concept revision  
✅ Self-learning and curiosity-based exploration

## ⚙️ Setup Instructions
### Step 1: Clone the Repository
```bash
git clone https://github.com/pankaj-kaushik/genai-labs.git
cd study-buddy
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
⚠️ Never commit .env to GitHub.

## ▶️ How to Run the Project
### Run main.py
```bash
python main.py
```

## 🧠 Prompt Used
```text
You are an expert Study Buddy. 
    1. Explain the concept of '{topic}' in simple terms (suitable for a 10-year-old).
    2. Use an analogy to make it memorable.
    3. Provide 3 bullet points of key takeaways.
    4. Generate 2 multiple-choice questions to test the user's understanding.
```

## 📌 Sample Output
Hey there! I'm your **Study Buddy**, and I’m here to help you understand the amazing world of AI. Let

### 1. What is AI?
AI stands for **Artificial Intelligence**.

Usually, computers are like calculators: they only do exactly what you tell them to do. If you don't 

**AI is different.** It is a type of computer program that can "think" and "learn" almost like a humaks at a massive amount of information (data), finds patterns, and learns how to solve problems or mak

---

### 2. The Memorable Analogy: The "Pro-Gamer" Apprentice
Imagine you want to teach a friend how to play a new video game, but they’ve never seen a controller 

*   **A Regular Computer** would need you to explain every single button press: *"Press A to jump. Prmy appeared that you didn't explain, the computer wouldn't know what to do.
*   **AI** is like an apprentice who watches you play for 100 hours. It notices that every time a lav
makes the score go up. Eventually, the AI says, *"I've got this!"* and starts playing the game by its

---

### 3. Key Takeaways
*   **AI Learns from Data:** Just like you learn from reading books or watching teachers, AI learns b
*   **It’s a Pattern-Finder:** AI is really good at spotting things humans might miss, like finding a
*   **It’s a Tool, Not a Person:** Even though it seems "smart," AI doesn't have feelings or a soul; 

---

### 4. Test Your Knowledge!

**Question 1: How does an AI usually get "smarter"?**
*   A) By taking a nap.
*   B) By looking at lots of examples and finding patterns.
*   C) By being plugged into a lemon.
*   D) It doesn't; it knows everything the moment it is turned on.

**Question 2: What makes AI different from a regular computer program?**
*   A) It can learn and make decisions without being told every single step.
*   B) It is made of actual human brain cells.
*   C) It is always a robot that looks like a person.
*   D) It doesn't need electricity to work.

***

**Answers:**

**Question 2: What makes AI different from a regular computer program?**
*   A) It can learn and make decisions without being told every single step.
*   B) It is made of actual human brain cells.
*   C) It is always a robot that looks like a person.
*   D) It doesn't need electricity to work.

***

**Answers:**
**Question 2: What makes AI different from a regular computer program?**
*   A) It can learn and make decisions without being told every single step.
*   B) It is made of actual human brain cells.
*   C) It is always a robot that looks like a person.
*   D) It doesn't need electricity to work.

***

**Answers:**
*   B) It is made of actual human brain cells.
*   C) It is always a robot that looks like a person.
*   D) It doesn't need electricity to work.

***

**Answers:**
*   D) It doesn't need electricity to work.

***

**Answers:**
***

**Answers:**

**Answers:**
*Q1: B | Q2: A*
**Answers:**
*Q1: B | Q2: A*
*Q1: B | Q2: A*

## ✨ Future Enhancements
- Difficulty level selection (Beginner/Intermediate/Advanced)
- Hindi/Multi-language explanation support
- Chat-style conversation 
- Add Streamlit web UI
- Save summaries to file (text/pdf)

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