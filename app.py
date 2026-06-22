from fastapi import FastAPI
from pydantic import BaseModel

from orchestrator import app as graph_app   # IMPORTANT: LangGraph compiled app


app = FastAPI(
    title="AI Database Agent (LangGraph)",
    version="2.0"
)


class QueryRequest(BaseModel):
    question: str



@app.get("/")
def health():
    return {
        "status": "running"
    }



@app.post("/ask")
def ask_question(request: QueryRequest):

    # Run LangGraph pipeline
    result = graph_app.invoke({
        "question": request.question
    })

    return {
        "question": request.question,
        "sql": result.get("sql"),
        "result": result.get("result"),
        "answer": result.get("final_answer"),
        "error": result.get("error")
    }