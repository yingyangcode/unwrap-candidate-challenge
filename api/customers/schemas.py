from pydantic import BaseModel, EmailStr, Field


class CustomerCreateSchema(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    email: EmailStr
    customer_id: str = Field(min_length=1, max_length=20, pattern=r'^CUST\d{3}$')


class CustomerResponseSchema(BaseModel):
    name: str
    email: EmailStr
    customer_id: str