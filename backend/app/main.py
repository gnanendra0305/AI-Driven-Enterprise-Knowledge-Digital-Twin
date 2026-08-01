from fastapi import FastAPI
from sqlalchemy import text

from app.database.connection import engine
from app.database.base import Base

# Import models so SQLAlchemy knows about them
from app.models.organization import Organization
from app.models.user import User
from app.models.department import Department
from app.models.document import Document
Base.metadata.create_all(bind=engine)

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