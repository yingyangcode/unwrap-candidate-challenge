from pydantic import BaseModel, EmailStr


class CustomerCreateSchema(BaseModel):
    name: str
    email: EmailStr
    customer_id: str


class CustomerResponseSchema(BaseModel):
    name: str
    email: EmailStr
    customer_id: str