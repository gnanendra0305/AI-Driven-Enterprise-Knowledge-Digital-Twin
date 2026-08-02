from sqlalchemy.orm import Session

from app.models.department import Department
from app.schemas.department import (
    DepartmentCreate,
    DepartmentUpdate
)


def create_department(
    db: Session,
    department: DepartmentCreate
):
    db_department = Department(
        name=department.name,
        description=department.description,
        organization_id=department.organization_id
    )

    db.add(db_department)
    db.commit()
    db.refresh(db_department)

    return db_department


def get_departments(db: Session):
    return db.query(Department).all()


def get_department(
    db: Session,
    department_id: int
):
    return (
        db.query(Department)
        .filter(Department.id == department_id)
        .first()
    )


def update_department(
    db: Session,
    department_id: int,
    department: DepartmentUpdate
):
    db_department = (
        db.query(Department)
        .filter(Department.id == department_id)
        .first()
    )

    if not db_department:
        return None

    update_data = department.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(db_department, key, value)

    db.commit()
    db.refresh(db_department)

    return db_department


def delete_department(
    db: Session,
    department_id: int
):
    db_department = (
        db.query(Department)
        .filter(Department.id == department_id)
        .first()
    )

    if not db_department:
        return None

    db.delete(db_department)
    db.commit()

    return db_department