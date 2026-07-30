import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env file")

client = genai.Client(api_key=api_key)


def code_assistant(task, language, code):
    prompt = f"""
You are an expert Software Engineer and AI Coding Assistant.

Task:
{task}

Programming Language:
{language}

Code:
{code}

Instructions:

- If the task is Generate Code, create clean and efficient code.
- If Debug Code, identify errors and provide corrected code.
- If Explain Code, explain each important part in simple language.
- If Optimize Code, improve readability and performance.
- If Generate Documentation, write professional documentation.
- If Review Code, identify issues and suggest improvements.
- Follow best coding practices.
- Return code inside proper markdown code blocks where appropriate.
"""

    try:
        response = client.models.generate_content(
            model="gemini-3.6-flash",
            contents=prompt
        )
        return response.text

    except Exception as e:
        return f"Error: {e}"