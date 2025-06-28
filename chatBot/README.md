# 🚀 Real Estate ChatBot Backend

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100.0-0?logo=fastapi&logoColor=white&label=FastAPI)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-%209.6-blue?logo=postgresql&logoColor=white)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)
![License](https://img.shields.io/badge/License-MIT-blue.svg)

---

## 🧠 About the Project

Welcome to the **Real Estate ChatBot Backend** – a high-performance, asynchronous backend built with **FastAPI**, powered by **Python** and **PostgreSQL**.

> ⚡️ This backend powers a chatbot that delivers real-time and historical real estate information, providing fast, accurate responses to property-related queries anytime.

---

## 🛠 Tech Stack

| Technology  | Description                  |
|-------------|------------------------------|
| 🐍 Python   | Core programming language     |
| ⚡ FastAPI   | Web framework for APIs        |
| 🐘 PostgreSQL | Relational Database System   |
| 🔐 Pydantic  | Data validation and parsing   |

---

## 🌐 Project Structure

```bash
.
app/
├── main.py                # Entry point
├── routes/                # API routes
│   └── chat.py
├── models/                # Database models
├── schemas/               # Pydantic schemas
├── services/              # Business logic
│   ├── create_real_estate_query.py
│   ├── is_real_estate_query.py
│   ├── is_realtime_query.py
│   ├── lama_service.py
│   └── perplexity_service.py
├── database.py            # Database connection
├── crud.py                # CRUD operations
├── __init__.py
tests/                     # Test cases
requirements.txt           # Python dependencies
.env                       # Environment variables
README.md                  # Project overview
