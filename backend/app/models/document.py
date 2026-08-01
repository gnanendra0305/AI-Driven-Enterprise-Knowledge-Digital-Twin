from datetime import datetime

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship

from app.database.base import Base


class Document(Base):
    __tablename__ = "documents"

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String(255), nullable=False)

    file_name = Column(String(255), nullable=False)

    file_path = Column(String(500), nullable=False)

    file_type = Column(String(20), nullable=False)

    file_size = Column(Integer)

    status = Column(String(50), default="uploaded")

    organization_id = Column(
        Integer,
        ForeignKey("organizations.id"),
        nullable=False
    )

    department_id = Column(
        Integer,
        ForeignKey("departments.id"),
        nullable=False
    )

    uploaded_by = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    updated_at = Column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )

    organization = relationship(
        "Organization",
        back_populates="documents"
    )

    department = relationship(
        "Department",
        back_populates="documents"
    )

    user = relationship(
        "User",
        back_populates="documents"
    )