from pydantic import BaseModel, Field, field_validator
from datetime import date, timedelta
from app.config import LibraryConfig


class CheckoutCreateSchema(BaseModel):
    isbn: str = Field(min_length=1, max_length=20)
    customer_id: str = Field(min_length=1, max_length=20, pattern=r'^CUST\d{3}$')
    due_date: str = Field(min_length=1, max_length=10)

    @field_validator("due_date")
    @classmethod
    def due_date_must_be_in_future(cls, v):
        try:
            due = date.fromisoformat(v)
        except ValueError:
            raise ValueError("Invalid date format. Use YYYY-MM-DD")
        
        today = date.today()
        
        if due < today:
            raise ValueError("Due date must be in the future")
        
        # Maximum loan period from config
        max_due_date = today + timedelta(days=LibraryConfig.MAX_LOAN_PERIOD_DAYS)
        if due > max_due_date:
            raise ValueError(f"Due date cannot be more than {LibraryConfig.MAX_LOAN_PERIOD_DAYS} days in the future")
        
        return v


class CheckoutResponseSchema(BaseModel):
    checkout_id: str
    isbn: str
    title: str
    customer_id: str
    checkout_date: str
    due_date: str


class ReturnCreateSchema(BaseModel):
    isbn: str = Field(min_length=1, max_length=20)
    customer_id: str = Field(min_length=1, max_length=20, pattern=r'^CUST\d{3}$')


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
