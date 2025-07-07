from pydantic import BaseModel, EmailStr


class Customer(BaseModel):
    name: str
    email: EmailStr
    customer_id: str
    
    class Config:
        frozen = True