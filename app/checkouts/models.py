from pydantic import BaseModel
from typing import Optional


class Checkout(BaseModel):
    checkout_id: str
    isbn: str
    customer_id: str
    checkout_date: str
    due_date: str
    return_date: Optional[str] = None
    
    @property
    def is_active(self) -> bool:
        return self.return_date is None
    
    @property
    def is_returned(self) -> bool:
        return self.return_date is not None
    
    class Config:
        frozen = True


class CheckoutWithTitle(BaseModel):
    checkout_id: str
    isbn: str
    customer_id: str
    checkout_date: str
    due_date: str
    title: str
    return_date: Optional[str] = None