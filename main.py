import os
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

def main():
    api_key = os.environ.get("GEMINI_API_KEY")
    if api_key == None:
        raise RuntimeError("API-Key not found!")
    client = genai.Client(api_key=api_key)

    # parse user prompt
    parser = argparse.ArgumentParser(description="Jarvis")
    parser.add_argument("user_prompt", type=str, help="User input")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()

    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]

    # Gemini call
    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=messages
    )

    # Prints
    if args.verbose == True:
        print("User prompt:",args.user_prompt)
        if response.usage_metadata != None:
            print("Prompt tokens:",response.usage_metadata.prompt_token_count)
            print("Response tokens:",response.usage_metadata.candidates_token_count)
    print("Response:")
    print(response.text)

    


if __name__ == "__main__":
    main()
