from llama_index.core import Settings

from app.llamaindex.llm import get_llm
from app.llamaindex.embeddings import get_embedding_model


def configure_llamaindex():
    Settings.llm = get_llm()
    Settings.embed_model = get_embedding_model()