"""
Text Summarizer - An AI-Powered Text Summarization Tool

This module provides functionality to automatically summarize text documents
using Google's Gemini API. It reads text from files, processes them through
the Gemini model, and generates concise summaries in bullet-point format.

Usage:
    python main.py
    
Requirements:
    - google-genai library
    - python-dotenv library
    - GEMINI_API_KEY environment variable
    - input.txt file in the same directory
"""

# Summarizer.py
# A simple script to demonstrate the use of Google Gen AI API for text summarization.
# It initializes the environment, creates a client, and generates a summary for a given text.
# Make sure to set the GEMINI_API_KEY in your environment variables.
# User Text (from file) -> Python Code -> Gemini API -> Summary Output(written to file)

from dotenv import load_dotenv
from google import genai
import os

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

def summarize_text(client, input_prompt):
    """
    Generates a text summary using the Gemini API.
    
    This function sends the provided prompt to the Gemini model and returns
    the generated summary. It includes comprehensive error handling for API
    failures and network issues.
    
    Args:
        client (genai.Client): An authenticated GenAI client instance.
        input_prompt (str): The prompt containing the text to be summarized.
        
    Returns:
        str: The AI-generated summary of the input text.
             Returns an error message string if the API call fails.
             
    Raises:
        No exceptions are raised; errors are caught and returned as strings.
    """
    try:
        response = client.models.generate_content(
            model="gemini-3-flash-preview", contents=input_prompt
        )
        return response.text
    except ValueError as ve:
        error_msg = f"Invalid input or API configuration error: {ve}"
        print(f"Error: {error_msg}")
        return error_msg
    except AttributeError as ae:
        error_msg = f"API response format error: {ae}"
        print(f"Error: {error_msg}")
        return error_msg
    except ConnectionError as ce:
        error_msg = f"Connection error while calling Gemini API: {ce}"
        print(f"Error: {error_msg}")
        return error_msg
    except TimeoutError as te:
        error_msg = f"API request timed out: {te}"
        print(f"Error: {error_msg}")
        return error_msg
    except Exception as e:
        error_msg = f"An unexpected error occurred while calling Gemini API: {e}"
        print(f"Error: {error_msg}")
        return error_msg

def read_text_from_file(file_path):
    """
    Reads text content from a file with relative or absolute path support.
    
    If a relative path is provided, it is treated as relative to this script's
    directory. This function includes error handling for missing files.
    
    Args:
        file_path (str): The path to the file (relative or absolute).
        
    Returns:
        str: The complete text content of the file.
        
    Raises:
        FileNotFoundError: If the specified file cannot be found.
    """
    # If a relative path is provided, treat it as relative to this script's directory.
    if not os.path.isabs(file_path):
        base_dir = os.path.dirname(__file__)
        file_path = os.path.join(base_dir, file_path)

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"Could not find input file at: {file_path}")

def create_prompt(user_text):
    """
    Constructs a prompt for the Gemini model to summarize text.
    
    Creates a detailed instruction set that guides Gemini to produce a
    professional, easy-to-understand summary in bullet-point format.
    
    Args:
        user_text (str): The text content to be summarized.
        
    Returns:
        str: A formatted prompt string with summarization instructions.
    """
    prompt = f"You are a professional editor. Summarize the following text in simple language.\nUse 4-5 bullet points.\nMake it easy for beginners to understand.\n{user_text}"
    return prompt

def initialize_environment():
    """
    Initializes the application environment.
    
    This function loads environment variables from a .env file using python-dotenv.
    The GEMINI_API_KEY is loaded from the environment and will be used by the
    GenAI client for authentication.
    """
    # Initialize environment variables
    print("Loading environment variables...")
    load_dotenv()

    # The client gets the API key from the environment variable `GEMINI_API_KEY`.
    # print("API KEY:", os.getenv("GEMINI_API_KEY"))

def main():
    """
    Main entry point for the Text Summarizer application.
    
    This function orchestrates the text summarization workflow:
    1. Displays a welcome message
    2. Initializes the environment and API client
    3. Reads text content from the input.txt file
    4. Creates a summarization prompt
    5. Generates a summary using the Gemini API
    6. Displays the generated summary
    """
    print("--- Welcome to your Text Summarizer Writer! ---")
    initialize_environment()
    print("Reading input text from file...")    
    user_text = read_text_from_file('input.txt')
    
    print("Creating prompt...")
    input_prompt = create_prompt(user_text)
    print(input_prompt)

    client = create_genai_client()
    print("Generating summary...")
        
    summary = summarize_text(client, input_prompt)
    print("Summary:", summary)

if __name__ == "__main__":
    main()  
    