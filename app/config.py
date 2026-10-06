import os

from dotenv import load_dotenv


load_dotenv()


GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
POSTGRES_URL = os.getenv("POSTGRES_URL")
API_KEY = os.getenv("API_KEY")

MAX_FILE_SIZE = 10 * 1024 * 1024
MODEL="gemini-3.1-flash-lite"

if not GEMINI_API_KEY:
    raise RuntimeError(
        "GEMINI_API_KEY is not configured."
    )

if not POSTGRES_URL:
    raise RuntimeError(
        "POSTGRES_URL is not configured."
    )