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
    
    # Extract the user's query from the request
    query = request.query

    # Check if the query is related to real estate
    if is_real_estate_query(query):
        # Get the current timestamp for logging purposes
        current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Determine if the query is requesting real-time information
        if is_realtime_query(query):
            # Prepare the query to ensure the best possible real-time response
            query = create_real_estate_query(query)
            # Send the query to the Perplexity AI service for live data
            content = perplexity_service(query)
        else:
            query = create_real_estate_query(query)

        # Refine the query further for LLaMA by wrapping the content into a precise summary instruction
        query = (
            "Based on the following information, generate a precise, well-structured summary or result. "
            "Highlight key insights, use bullet points or sections where helpful, and ensure clarity and accuracy. "
            "Here is the information:\n\n" + content
        )

        # Send the refined query to the LLaMA service for structured response generation
        content = lama_service(query)

        # Save the chat history to the database for future reference or analytics
        crud.save_chat_history(db, time=current_datetime, query=query, response=content)

        # Return the generated response to the client
        return {"response": content}

    # If the query is unrelated to real estate, return a polite rejection message
    return {"response": "Thank you for reaching out. I can only assist with property-related questions."}

@router.get("/show-responses/{page}", response_model=list[ChatHistoryOut])
def get_responses(
    page: int = Path(..., ge=1),
    limit: int = 10,
    db: Session = Depends(get_db)
):
    offset = (page - 1) * limit
    return crud.get_chat_history(db, skip=offset, limit=limit)
