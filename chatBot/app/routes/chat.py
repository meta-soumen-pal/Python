from fastapi import APIRouter, Depends, Path
from sqlalchemy.orm import Session
from together import Together
from datetime import datetime
import os
from pydantic import BaseModel

from ..database import SessionLocal
from ..schemas import ChatHistoryOut
from .. import crud

from app.services.lama_service import lama_service
from app.services.perplexity_service import perplexity_service
from app.services. is_realtime_query import is_realtime_query
from app.services.is_real_estate_query import is_real_estate_query
from app.services.create_real_estate_query import create_real_estate_query






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


class ChatRequest(BaseModel):
    query: str
    
    
@router.post("/chat")
def chat(request: ChatRequest, db: Session = Depends(get_db)):
    
    query = request.query
    # Check query is related to real_estate or not
    if is_real_estate_query(query):
        current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # If query is related to real tine then hand over to perplexity otherwise lama
        if is_realtime_query(query):
            # Prepare query for best result
            query = create_real_estate_query(query)
            # Call perplexity ai
            content = perplexity_service(query)
        else:
            # Prepare query for best result
            query = create_real_estate_query(query)
             # Call perplexity ai
            content = lama_service(query)
        # Save query to data base
        crud.save_chat_history(db, time=current_datetime, query=query, response=content)
        #return content
        return {"response": content}
    # If inside query some real estate key word not present then return this
    return {"response": "Thank you for reaching out. I can only assist with property-related questions."}


@router.get("/show-responses/{page}", response_model=list[ChatHistoryOut])
def get_responses(
    page: int = Path(..., ge=1),
    limit: int = 10,
    db: Session = Depends(get_db)
):
    offset = (page - 1) * limit
    return crud.get_chat_history(db, skip=offset, limit=limit)
