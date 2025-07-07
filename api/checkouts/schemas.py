from pydantic import BaseModel


class CheckoutCreateSchema(BaseModel):
    isbn: str
    customer_id: str
    due_date: str


class CheckoutResponseSchema(BaseModel):
    checkout_id: str
    isbn: str
    title: str
    customer_id: str
    checkout_date: str
    due_date: str


class ReturnCreateSchema(BaseModel):
    isbn: str
    customer_id: str


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