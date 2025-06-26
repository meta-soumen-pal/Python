from pydantic import BaseModel

class ChatHistoryOut(BaseModel):
    time: str
    query: str
    response: str

    class Config:
        orm_mode = True
