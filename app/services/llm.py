from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

def get_llm():
    return GoogleGenerativeAI(
        model="gemini-3.1-flash-lite",
        temperature=0
    )