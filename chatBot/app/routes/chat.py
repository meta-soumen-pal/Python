from fastapi import APIRouter, Depends, Path
from sqlalchemy.orm import Session
from together import Together
from datetime import datetime
import os
from dotenv import load_dotenv

from ..database import SessionLocal
from ..schemas import ChatHistoryOut
from .. import crud

load_dotenv()
router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
def hello():
    return {"message": "Welcome to chat app"}

@router.post("/chat/{query}")
def chat(query: str, db: Session = Depends(get_db)):
    client = Together(api_key=os.getenv("LAMA_API_KEY"))
    current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    response = client.chat.completions.create(
        model="meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8",
        messages=[{"role": "user", "content": f"{query} in markdown format"}]
    )

    content = response.choices[0].message.content
    crud.save_chat_history(db, time=current_datetime, query=query, response=content)
    return {"response": content}

@router.get("/show-responses/{page}", response_model=list[ChatHistoryOut])
def get_responses(
    page: int = Path(..., ge=1),
    limit: int = 10,
    db: Session = Depends(get_db)
):
    offset = (page - 1) * limit
    return crud.get_chat_history(db, skip=offset, limit=limit)
