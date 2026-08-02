from sqlalchemy.orm import Session

from app.models.document import Document
from app.schemas.document import (
    DocumentCreate,
    DocumentUpdate
)


def create_document(
    db: Session,
    document: DocumentCreate
):
    db_document = Document(
        title=document.title,
        file_name=document.file_name,
        file_path=document.file_path,
        file_type=document.file_type,
        file_size=document.file_size,
        status=document.status,
        organization_id=document.organization_id,
        department_id=document.department_id,
        uploaded_by=document.uploaded_by
    )

    db.add(db_document)
    db.commit()
    db.refresh(db_document)

    return db_document


def get_documents(db: Session):
    return db.query(Document).all()


def get_document(
    db: Session,
    document_id: int
):
    return (
        db.query(Document)
        .filter(Document.id == document_id)
        .first()
    )


def update_document(
    db: Session,
    document_id: int,
    document: DocumentUpdate
):
    db_document = (
        db.query(Document)
        .filter(Document.id == document_id)
        .first()
    )

    if not db_document:
        return None

    update_data = document.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(db_document, key, value)

    db.commit()
    db.refresh(db_document)

    return db_document


def delete_document(
    db: Session,
    document_id: int
):
    db_document = (
        db.query(Document)
        .filter(Document.id == document_id)
        .first()
    )

    if not db_document:
        return None

    db.delete(db_document)
    db.commit()

    return db_document