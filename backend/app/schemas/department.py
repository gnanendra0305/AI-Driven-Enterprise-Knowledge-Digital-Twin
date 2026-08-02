from pydantic import BaseModel, ConfigDict
from datetime import datetime


class DepartmentBase(BaseModel):
    name: str
    description: str
    organization_id: int


class DepartmentCreate(DepartmentBase):
    pass


class DepartmentUpdate(BaseModel):
    name: str | None = None
    description: str | None = None
    organization_id: int | None = None


class DepartmentResponse(DepartmentBase):
    id: int
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)