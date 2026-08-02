from pydantic import BaseModel, ConfigDict, EmailStr


class UserBase(BaseModel):
    full_name: str
    email: EmailStr
    role: str
    organization_id: int


class UserCreate(UserBase):
    password: str


class UserUpdate(BaseModel):
    full_name: str | None = None
    email: EmailStr | None = None
    password: str | None = None
    role: str | None = None
    organization_id: int | None = None


class UserResponse(UserBase):
    id: int

    model_config = ConfigDict(from_attributes=True)