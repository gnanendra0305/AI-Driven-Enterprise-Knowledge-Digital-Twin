from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.session import get_db

from app.crud.department import (
    create_department,
    get_departments,
    get_department,
    update_department,
    delete_department
)

from app.schemas.department import (
    DepartmentCreate,
    DepartmentUpdate,
    DepartmentResponse
)

router = APIRouter(
    prefix="/departments",
    tags=["Departments"]
)


@router.post(
    "/",
    response_model=DepartmentResponse
)
def create_new_department(
    department: DepartmentCreate,
    db: Session = Depends(get_db)
):
    return create_department(db, department)


@router.get(
    "/",
    response_model=List[DepartmentResponse]
)
def read_departments(
    db: Session = Depends(get_db)
):
    return get_departments(db)


@router.get(
    "/{department_id}",
    response_model=DepartmentResponse
)
def read_department(
    department_id: int,
    db: Session = Depends(get_db)
):
    department = get_department(db, department_id)

    if department is None:
        raise HTTPException(
            status_code=404,
            detail="Department not found"
        )

    return department


@router.put(
    "/{department_id}",
    response_model=DepartmentResponse
)
def update_existing_department(
    department_id: int,
    department: DepartmentUpdate,
    db: Session = Depends(get_db)
):
    updated = update_department(
        db,
        department_id,
        department
    )

    if updated is None:
        raise HTTPException(
            status_code=404,
            detail="Department not found"
        )

    return updated


@router.delete(
    "/{department_id}",
    response_model=DepartmentResponse
)
def delete_existing_department(
    department_id: int,
    db: Session = Depends(get_db)
):
    deleted = delete_department(
        db,
        department_id
    )

    if deleted is None:
        raise HTTPException(
            status_code=404,
            detail="Department not found"
        )

    return deleted