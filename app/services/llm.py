from langchain_google_genai import ChatGoogleGenerativeAI

from app.config import GEMINI_API_KEY, MODEL


llm = ChatGoogleGenerativeAI(
    model=MODEL,
    temperature=0,
    google_api_key=GEMINI_API_KEY
)