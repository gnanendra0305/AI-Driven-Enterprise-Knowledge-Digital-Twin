from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas.user import (
    UserCreate,
    UserUpdate
)


def create_user(
    db: Session,
    user: UserCreate
):
    db_user = User(
        full_name=user.full_name,
        email=user.email,
        password=user.password,
        role=user.role,
        organization_id=user.organization_id
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user


def get_users(db: Session):
    return db.query(User).all()


def get_user(
    db: Session,
    user_id: int
):
    return (
        db.query(User)
        .filter(User.id == user_id)
        .first()
    )


def update_user(
    db: Session,
    user_id: int,
    user: UserUpdate
):
    db_user = (
        db.query(User)
        .filter(User.id == user_id)
        .first()
    )

    if not db_user:
        return None

    update_data = user.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(db_user, key, value)

    db.commit()
    db.refresh(db_user)

    return db_user


def delete_user(
    db: Session,
    user_id: int
):
    db_user = (
        db.query(User)
        .filter(User.id == user_id)
        .first()
    )

    if not db_user:
        return None

    db.delete(db_user)
    db.commit()

    return db_user