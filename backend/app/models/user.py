from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.database.base import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    full_name = Column(String(200), nullable=False)

    email = Column(String(200), unique=True, nullable=False)

    password = Column(String(255), nullable=False)

    role = Column(String(50), nullable=False)

    organization_id = Column(
        Integer,
        ForeignKey("organizations.id")
    )

    organization = relationship(
        "Organization",
        back_populates="users"
    )

    documents = relationship(
        "Document",
        back_populates="user"
    )