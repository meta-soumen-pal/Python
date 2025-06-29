from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes import chat
from .models import Base
from .database import engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(chat.router)
