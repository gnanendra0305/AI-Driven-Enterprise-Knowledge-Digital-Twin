from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.session import get_db

from app.crud.document import (
    create_document,
    get_documents,
    get_document,
    update_document,
    delete_document
)

from app.schemas.document import (
    DocumentCreate,
    DocumentUpdate,
    DocumentResponse
)

router = APIRouter(
    prefix="/documents",
    tags=["Documents"]
)


@router.post(
    "/",
    response_model=DocumentResponse
)
def create_new_document(
    document: DocumentCreate,
    db: Session = Depends(get_db)
):
    return create_document(db, document)


@router.get(
    "/",
    response_model=List[DocumentResponse]
)
def read_documents(
    db: Session = Depends(get_db)
):
    return get_documents(db)


@router.get(
    "/{document_id}",
    response_model=DocumentResponse
)
def read_document(
    document_id: int,
    db: Session = Depends(get_db)
):
    document = get_document(db, document_id)

    if document is None:
        raise HTTPException(
            status_code=404,
            detail="Document not found"
        )

    return document


@router.put(
    "/{document_id}",
    response_model=DocumentResponse
)
def update_existing_document(
    document_id: int,
    document: DocumentUpdate,
    db: Session = Depends(get_db)
):
    updated = update_document(
        db,
        document_id,
        document
    )

    if updated is None:
        raise HTTPException(
            status_code=404,
            detail="Document not found"
        )

    return updated


@router.delete(
    "/{document_id}",
    response_model=DocumentResponse
)
def delete_existing_document(
    document_id: int,
    db: Session = Depends(get_db)
):
    deleted = delete_document(
        db,
        document_id
    )

    if deleted is None:
        raise HTTPException(
            status_code=404,
            detail="Document not found"
        )

    return deleted