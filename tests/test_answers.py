from app.agents.service import ask_agent
from tests.evaluation_dataset import EVALUATION_DATASET


def test_answers():

    for index, item in enumerate(EVALUATION_DATASET):

        thread_id = f"evaluation-{index}"

        result = ask_agent(
            question=item["question"],
            thread_id=thread_id
        )

        answer = result["answer"]

        print("\nQuestion:")
        print(item["question"])

        print("\nExpected:")
        print(item["expected_answer"])

        print("\nActual:")
        print(answer)

        assert answer