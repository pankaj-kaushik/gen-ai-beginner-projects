"""
Email Writer - An AI-Powered Email and Message Generation Assistant

This module provides an interactive way to generate professional and personalized
emails and messages using Google's Gemini API. It helps users create well-crafted
communications tailored to specific purposes, tones, and recipients.

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

def create_email_prompt(purpose, tone, recipient, key_points):
    """
    Constructs a structured prompt for generating personalized emails.
    
    This function creates a detailed prompt that instructs Gemini to generate
    professional and engaging emails based on user specifications.
    
    Args:
        purpose (str): The main purpose or intent of the email.
        tone (str): The desired tone (e.g., formal, casual, enthusiastic).
        recipient (str): Description of the recipient or recipient type.
        key_points (str): Key points to include in the email.
        
    Returns:
        str: A formatted prompt string with instructions for the AI model.
    """
    # We use a system-style prompt to guide Gemini's behavior
    prompt = f"""
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

def get_user_input():
    """
    Collects email composition details from the user via interactive prompts.
    
    Returns:
        tuple: A tuple containing:
            - purpose (str): The main purpose of the email
            - tone (str): The desired tone for the email
            - recipient (str): Details about the recipient
            - key_points (str): Key points to include in the email
    """
    purpose = input("Enter purpose of the email or message: ")
    tone = input("Enter desired tone (e.g., formal, casual, enthusiastic): ")
    recipient = input("Enter recipient details (e.g., friend, colleague, client): ")
    key_points = input("Enter key points to include (separated by commas): ")
    return purpose, tone, recipient, key_points

def generate_email(client, prompt):
    """
    Generates an email or message using the Gemini API.
    
    This function sends the composed prompt to the Gemini model with specific
    system instructions to ensure high-quality, professional email generation.
    It includes error handling for API failures.
    
    Args:
        client (genai.Client): An authenticated GenAI client instance.
        prompt (str): The formatted prompt containing purpose, tone, recipient, and key points.
        
    Returns:
        str: The AI-generated email or message content.
             If an error occurs, returns an error message string.
    """
    system_instructions = "You are a helpful assistant that writes emails and messages."
    try:
        response = client.models.generate_content(
            model="gemini-3-flash-preview",  # Using the fast and capable flash model
            config=genai.types.GenerateContentConfig(system_instruction=system_instructions),
            contents=prompt
        )
        return response.text
    except Exception as e:
        return f"An error occurred: {e}"

def main():
    """
    Main entry point for the Email Writer application.
    
    This function orchestrates the email generation workflow:
    1. Displays a welcome message
    2. Initializes the environment and API client
    3. Collects email specifications from the user
    4. Generates a customized, professional email based on user input
    5. Displays the generated email in a formatted manner
    """
    print("--- Welcome to your AI Email & Message Writer! ---")
    initialize_environment()
    print("Please provide details for the email/message you want to create.")
    purpose, tone, recipient, key_points = get_user_input()
    print("Creating Email Prompt...")
    user_prompt = create_email_prompt(purpose, tone, recipient, key_points)
    client = create_genai_client()
    print("Generating email/message... Please wait.\n")
    result = generate_email(client, user_prompt)
    print("--- Generated Email/Message ---")
    print(result)
    print("-" * 30)

if __name__ == "__main__":
    main()