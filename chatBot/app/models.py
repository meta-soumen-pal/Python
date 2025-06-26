from sqlalchemy import Column, Integer, String
from .database import Base

class ChatBotHistory(Base):
    __tablename__ = "chat_history"

    id = Column(Integer, primary_key=True, index=True)
    time = Column(String)
    query = Column(String)
    response = Column(String)
