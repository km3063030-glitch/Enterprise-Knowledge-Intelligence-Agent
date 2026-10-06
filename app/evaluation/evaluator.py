from langchain_google_genai import ChatGoogleGenerativeAI

from app.config import GEMINI_API_KEY, MODEL

llm = ChatGoogleGenerativeAI(
    model=MODEL,
    temperature=0,
    google_api_key=GEMINI_API_KEY
)

EVALUATION_PROMPT = """
You are an expert evaluator for an enterprise RAG system.

Evaluate the generated answer using the question
and retrieved context.

Question:
{question}

Retrieved Context:
{context}

Generated Answer:
{answer}

Evaluate the answer on these dimensions:

1. Correctness:
Is the answer consistent with the retrieved context?

2. Groundedness:
Is the answer supported by information in the context?

3. Relevance:
Does the answer directly address the question?

Return ONLY valid JSON in this format:

{{
    "correct": true,
    "grounded": true,
    "relevant": true,
    "score": 5,
    "reason": "Short explanation"
}}

The score must be an integer from 1 to 5.
"""


def evaluate_answer(
    question: str,
    context: str,
    answer: str
):

    prompt = EVALUATION_PROMPT.format(
        question=question,
        context=context,
        answer=answer
    )

    response = llm.invoke(prompt)

    return response.content