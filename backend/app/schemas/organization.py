from pydantic import BaseModel, ConfigDict


class OrganizationBase(BaseModel):
    name: str
    industry: str


class OrganizationCreate(OrganizationBase):
    pass


class OrganizationUpdate(BaseModel):
    name: str | None = None
    industry: str | None = None


class OrganizationResponse(OrganizationBase):
    id: int

    model_config = ConfigDict(from_attributes=True)