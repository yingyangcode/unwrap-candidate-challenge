from abc import ABC, abstractmethod
from typing import List, Optional
from app.checkouts.models import Checkout


class CheckoutRepositoryInterface(ABC):
    @abstractmethod
    def create_checkout(self, isbn: str, customer_id: str, due_date: str) -> Checkout:
        pass
    
    @abstractmethod
    def get_active_by_customer(self, customer_id: str) -> List[Checkout]:
        pass
    
    @abstractmethod
    def mark_returned(self, isbn: str, customer_id: str) -> Optional[Checkout]:
        pass
    
    @abstractmethod
    def get_active_checkout(self, isbn: str, customer_id: str) -> Optional[Checkout]:
        pass