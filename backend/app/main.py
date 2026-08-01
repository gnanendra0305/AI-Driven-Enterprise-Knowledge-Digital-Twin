from fastapi import FastAPI
from sqlalchemy import text

from app.database.connection import engine

app = FastAPI(
    title="Enterprise Knowledge Digital Twin API",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "Enterprise Knowledge Digital Twin API is Running Successfully 🚀"
    }


@app.get("/db-test")
def db_test():
    with engine.connect() as connection:
        result = connection.execute(text("SELECT version();"))
        version = result.fetchone()

    return {
        "database": version[0]
    }