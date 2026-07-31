from fastapi import FastAPI
from pydantic import BaseModel

from app.generator import generate_answer

app = FastAPI(
    title="Support Knowledge Copilot",
    version="1.0"
)


class Question(BaseModel):
    question: str


@app.get("/")
def home():
    return {
        "message": "Support Knowledge Copilot API is running."
    }


@app.post("/ask")
def ask(question: Question):

    response = generate_answer(question.question)

    return response