from fastapi import FastAPI, Request
from langchain_logic import get_hr_answer
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # or ["*"] for all origins (dev only)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/ask")
async def ask_endpoint(request: Request):
    data = await request.json()
    question = data.get("question", "")
    answer = get_hr_answer(question)
    return {"answer": answer}