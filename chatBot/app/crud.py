from sqlalchemy.orm import Session
from . import models

def save_chat_history(db: Session, time: str, query: str, response: str):
    chat = models.ChatBotHistory(time=time, query=query, response=response)
    db.add(chat)
    db.commit()
    db.refresh(chat)
    return chat

def get_chat_history(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.ChatBotHistory).offset(skip).limit(limit).all()
