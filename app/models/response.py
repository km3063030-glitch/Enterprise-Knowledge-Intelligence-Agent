from pydantic import BaseModel
from typing import List


class Source(BaseModel):
    document: str
    page: int | str


class AgentResponse(BaseModel):
    answer: str
    sources: List[Source]