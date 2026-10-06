from llama_index.core import Document
from llama_index.core import VectorStoreIndex
from dotenv import load_dotenv

load_dotenv()

from app.llamaindex.config import configure_llamaindex

configure_llamaindex()


documents = [
    Document(
        text="""
        Employees receive 24 days of annual leave
        per calendar year.
        """
    ),
    Document(
        text="""
        Employees are expected to work 40 hours
        per week.
        """
    )
]


index = VectorStoreIndex.from_documents(documents)

query_engine = index.as_query_engine()

response = query_engine.query(
    "How many vacation days do employees receive?"
)

print(response)