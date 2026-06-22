from typing import TypedDict, Optional, Dict, Any


class GraphState(TypedDict):

    question: str

    schema: str

    sql: str

    result: Any

    error: Optional[str]

    final_answer: str