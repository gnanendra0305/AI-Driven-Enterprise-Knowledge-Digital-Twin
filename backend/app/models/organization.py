from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.database.base import Base


class Organization(Base):
    __tablename__ = "organizations"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String(200), nullable=False)

    industry = Column(String(100))

    users = relationship(
        "User",
        back_populates="organization"
    )

    departments = relationship(
        "Department",
        back_populates="organization"
    )

    documents = relationship(
        "Document",
        back_populates="organization"
    )