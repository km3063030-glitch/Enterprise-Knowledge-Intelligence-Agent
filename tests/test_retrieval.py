from app.retrieval.search import search_documents
from tests.evaluation_dataset import EVALUATION_DATASET


def test_retrieval():

    for item in EVALUATION_DATASET:

        documents = search_documents(
            item["question"],
            k=3
        )

        assert len(documents) > 0, (
            f"No documents retrieved for: "
            f"{item['question']}"
        )

        sources = [
            document.metadata.get("source", "")
            for document in documents
        ]

        print("\nQuestion:")
        print(item["question"])

        print("\nRetrieved sources:")
        for source in sources:
            print(source)

        assert any(
            item["expected_source"] in source
            for source in sources
        ), (
            f"Expected source not retrieved: "
            f"{item['expected_source']}"
        )