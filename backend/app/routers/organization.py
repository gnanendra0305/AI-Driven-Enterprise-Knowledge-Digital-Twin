from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.crud.organization import (
    create_organization,
    get_organizations,
    get_organization,
    update_organization,
    delete_organization,
)
from app.schemas.organization import (
    OrganizationCreate,
    OrganizationUpdate,
    OrganizationResponse,
)

router = APIRouter(
    prefix="/organizations",
    tags=["Organizations"]
)


@router.post(
    "/",
    response_model=OrganizationResponse
)
def create_new_organization(
    organization: OrganizationCreate,
    db: Session = Depends(get_db)
):
    return create_organization(db, organization)


@router.get(
    "/",
    response_model=List[OrganizationResponse]
)
def read_organizations(
    db: Session = Depends(get_db)
):
    return get_organizations(db)


@router.get(
    "/{organization_id}",
    response_model=OrganizationResponse
)
def read_organization(
    organization_id: int,
    db: Session = Depends(get_db)
):
    organization = get_organization(db, organization_id)

    if organization is None:
        raise HTTPException(
            status_code=404,
            detail="Organization not found"
        )

    return organization


@router.put(
    "/{organization_id}",
    response_model=OrganizationResponse
)
def update_existing_organization(
    organization_id: int,
    organization: OrganizationUpdate,
    db: Session = Depends(get_db)
):
    updated = update_organization(
        db,
        organization_id,
        organization
    )

    if updated is None:
        raise HTTPException(
            status_code=404,
            detail="Organization not found"
        )

    return updated


@router.delete(
    "/{organization_id}",
    response_model=OrganizationResponse
)
def delete_existing_organization(
    organization_id: int,
    db: Session = Depends(get_db)
):
    deleted = delete_organization(
        db,
        organization_id
    )

    if deleted is None:
        raise HTTPException(
            status_code=404,
            detail="Organization not found"
        )

    return deleted