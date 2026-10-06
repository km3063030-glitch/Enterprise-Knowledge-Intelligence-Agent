from app.evaluation.evaluator import evaluate_answer


def test_evaluator():

    question = "How many vacation days do employees receive?"

    context = """
    Employees receive 24 days of annual leave
    per calendar year.
    """

    answer = (
        "Employees receive 30 days of annual leave "
        "per calendar year."
    )

    result = evaluate_answer(
        question=question,
        context=context,
        answer=answer
    )

    print("\nEvaluation:")
    print(result)

    assert result