# 🤖 AI Email / Message Writer (Gemini LLM)

An AI-powered Email and Message Writing Assistant built using **Python** and **Google Gemini LLM**.  
This tool helps users generate professional, friendly, or persuasive emails/messages instantly based on purpose, tone, and key points.


This project helps learners quickly understand difficult topics without technical jargon.

This project is ideal for:
- Students 📚
- Working professionals 👨‍💻
- Content creators ✍️
- Anyone who wants quick insights from long articles

## 🚀 What This Project Does
- Generate professional emails/messages using AI
- Control tone (Formal, Friendly, Persuasive, etc.)
- Supports different recipient types (Client, Boss, Friend, etc.)
- CLI-based interface
- Modular and scalable architecture
- Easy to extend with new AI capabilities

## 🧩 Use Cases
✅ Writing professional emails
✅ Client communication drafts
✅ Follow-up messages
✅ Apology / Request emails
✅ Personal or casual message generation
✅ Productivity automation

## ⚙️ Setup Instructions
### Step 1: Clone the Repository
```bash
git clone https://github.com/pankaj-kaushik/genai-labs.git
cd email-writer
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
You are an expert Email and Message Writer.
1. Write an email or message with the following purpose: '{purpose}'.
2. Use a '{tone}' tone appropriate for the recipient: '{recipient}'.
3. Include the following key points: {key_points}.
4. Ensure the email/message is clear, concise, and engaging.

Guidelines
- Keep language natural and human-like
- Maintain clarity and professionalism
- Add proper greeting and closing
- Keep it concise but complete
Generate only the final email/message. 
```

## 📌 Sample Output
```text
--- Welcome to your AI Email & Message Writer! ---
Loading environment variables...
Please provide details for the email/message you want to create.
Enter purpose of the email or message: New Year Greeting
Enter desired tone (e.g., formal, casual, enthusiastic): Formal
Enter recipient details (e.g., friend, colleague, client): friend
Enter key points to include (separated by commas): best wishes for health and prosperity
Creating Email Prompt... 
Creating Gen AI client...
Generating email/message... Please wait.

--- Generated Email/Message ---
Subject: New Year Greetings and Best Wishes

Dear [Friend's Name],

As we transition into the new year, I wanted to take a moment to extend my sincere well wishes to you.

I hope the coming year brings you continued health, happiness, and great prosperity in all your endeavors. May it be a season of growth and success for you and your loved ones.

Best regards,

[Your Name]
------------------------------
```
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