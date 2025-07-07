from pydantic import BaseModel, EmailStr, Field


class CustomerCreateSchema(BaseModel):
    name: str = Field(min_length=1)
    email: EmailStr
    customer_id: str = Field(min_length=1)


class CustomerResponseSchema(BaseModel):
    name: str
    email: EmailStr
    customer_id: str