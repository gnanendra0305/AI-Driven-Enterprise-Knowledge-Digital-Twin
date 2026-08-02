from datetime import datetime

from pydantic import BaseModel, ConfigDict


class DocumentBase(BaseModel):
    title: str
    file_name: str
    file_path: str
    file_type: str
    file_size: int
    status: str
    organization_id: int
    department_id: int
    uploaded_by: int


class DocumentCreate(DocumentBase):
    pass


class DocumentUpdate(BaseModel):
    title: str | None = None
    file_name: str | None = None
    file_path: str | None = None
    file_type: str | None = None
    file_size: int | None = None
    status: str | None = None
    organization_id: int | None = None
    department_id: int | None = None
    uploaded_by: int | None = None


class DocumentResponse(DocumentBase):
    id: int
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)