from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings

load_dotenv()

def get_embedding_model():
    return GoogleGenerativeAIEmbeddings(
        model="gemini-embedding-001"
    )