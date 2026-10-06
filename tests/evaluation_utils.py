def normalize(text: str) -> str:
    return " ".join(text.lower().split())


def contains_expected_answer(
    answer: str,
    expected_answer: str
) -> bool:

    answer = normalize(answer)
    expected = normalize(expected_answer)

    return expected in answer