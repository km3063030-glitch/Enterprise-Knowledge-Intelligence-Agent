from llama_index.embeddings.google_genai import GoogleGenAIEmbedding


def get_embedding_model():
    return GoogleGenAIEmbedding(
        model_name="gemini-embedding-001"
    )