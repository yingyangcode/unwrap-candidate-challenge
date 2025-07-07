from pydantic import BaseModel, Field, field_validator
from datetime import date


class CheckoutCreateSchema(BaseModel):
    isbn: str = Field(min_length=1)
    customer_id: str = Field(min_length=1)
    due_date: str = Field(min_length=1)

    @field_validator("due_date")
    @classmethod
    def due_date_must_be_in_future(cls, v):
        due = date.fromisoformat(v)
        if due <= date.today():
            raise ValueError("Due date must be in the future")
        return v


class CheckoutResponseSchema(BaseModel):
    checkout_id: str
    isbn: str
    title: str
    customer_id: str
    checkout_date: str
    due_date: str


class ReturnCreateSchema(BaseModel):
    isbn: str = Field(min_length=1)
    customer_id: str = Field(min_length=1)


class ReturnResponseSchema(BaseModel):
    message: str
    isbn: str
    customer_id: str
    return_date: str


class CustomerBooksSchema(BaseModel):
    isbn: str
    title: str
    author: str
    checkout_date: str
    due_date: str
