from fastapi import FastAPI
from sqlalchemy import text

from app.database.connection import engine
from app.database.base import Base

# Import models
from app.models.organization import Organization
from app.models.user import User
from app.models.department import Department
from app.models.document import Document

# Import routers
from app.routers.organization import router as organization_router
from app.routers.user import router as user_router
from app.routers.department import router as department_router
from app.routers.document import router as document_router
# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Enterprise Knowledge Digital Twin API",
    version="1.0.0"
)

# Register routers
app.include_router(organization_router)
app.include_router(user_router)
app.include_router(department_router)
app.include_router(document_router)
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