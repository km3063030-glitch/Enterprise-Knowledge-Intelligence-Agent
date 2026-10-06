from pydantic import BaseModel, Field


class EvaluationResult(BaseModel):
    correct: bool
    grounded: bool
    relevant: bool
    score: int = Field(
        ge=1,
        le=5
    )
    reason: str