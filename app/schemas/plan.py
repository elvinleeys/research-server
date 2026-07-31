from pydantic import BaseModel
from typing import Literal

class Plan(BaseModel):
    task_type: Literal[
        "general",
        "summarize",
        "analyze_document",
        "research"
    ]

    steps: list[str]