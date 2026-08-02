from sqlalchemy.orm import Session

from app.models.organization import Organization
from app.schemas.organization import (
    OrganizationCreate,
    OrganizationUpdate
)


def create_organization(
    db: Session,
    organization: OrganizationCreate
):
    db_organization = Organization(
        name=organization.name,
        industry=organization.industry
    )

    db.add(db_organization)
    db.commit()
    db.refresh(db_organization)

    return db_organization


def get_organizations(db: Session):
    return db.query(Organization).all()


def get_organization(
    db: Session,
    organization_id: int
):
    return (
        db.query(Organization)
        .filter(Organization.id == organization_id)
        .first()
    )


def update_organization(
    db: Session,
    organization_id: int,
    organization: OrganizationUpdate
):
    db_organization = (
        db.query(Organization)
        .filter(Organization.id == organization_id)
        .first()
    )

    if not db_organization:
        return None

    update_data = organization.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(db_organization, key, value)

    db.commit()
    db.refresh(db_organization)

    return db_organization


def delete_organization(
    db: Session,
    organization_id: int
):
    db_organization = (
        db.query(Organization)
        .filter(Organization.id == organization_id)
        .first()
    )

    if not db_organization:
        return None

    db.delete(db_organization)
    db.commit()

    return db_organization