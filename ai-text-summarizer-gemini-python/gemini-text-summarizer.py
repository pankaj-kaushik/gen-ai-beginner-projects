
import os
from dotenv import load_dotenv
from google import genai
from prompts import BULLET_PROMPT, EXECUTIVE_PROMPT, ONE_LINE_PROMPT

# Load environment variables from .env file
load_dotenv()

# Constants
TARGET_MODEL = "gemini-3-flash-preview"
TARGET_FILE = "sample_article.txt"

def create_genai_client():
    """
    Initializes and returns a Google GenAI client.
    
    The client automatically uses the GEMINI_API_KEY from the environment
    to authenticate with Google's API.
    
    Returns:
        genai.Client: An authenticated GenAI client instance.
    """
    return genai.Client()

def create_summary(client, text, prompt_template):
    
    user_prompt = create_user_prompt(text, prompt_template)
    try:
        response = client.models.generate_content(
            model=TARGET_MODEL,
            contents=f"{user_prompt}"
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

    # If a relative path is provided, treat it as relative to this script's directory.
    if not os.path.isabs(file_path):
        base_dir = os.path.dirname(__file__)
        file_path = os.path.join(base_dir, file_path)

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"Could not find input file at: {file_path}")

def create_user_prompt(text, prompt_template):
    user_prompt = f"{prompt_template}\n{text}" 
    return user_prompt

def main():
    
    print("--- Welcome to your AI Text Summarizer! ---")
    print("Reading input text from file...")    
    user_text = read_text_from_file(TARGET_FILE)
    
    print("Generating Basic summary...Please wait...")
    
    client = create_genai_client()
    bullet_summary = create_summary(client, user_text, BULLET_PROMPT)
    print("\n--- Bullet Point Summary ---")
    print(bullet_summary)

    executive_summary = create_summary(client, user_text, EXECUTIVE_PROMPT)
    print("\n--- Executive Summary ---")
    print(executive_summary)

    one_line_summary = create_summary(client, user_text, ONE_LINE_PROMPT)
    print("\n--- One Line Summary ---")
    print(one_line_summary)

if __name__ == "__main__":
    main()  
    