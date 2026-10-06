from llama_index.llms.google_genai import GoogleGenAI
from dotenv import load_dotenv

load_dotenv()

def get_llm():
    return GoogleGenAI(
        model="gemini-3.1-flash-lite"
    )