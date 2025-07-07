from abc import ABC, abstractmethod
from typing import Optional
from app.customers.models import Customer


class CustomerRepositoryInterface(ABC):
    @abstractmethod
    def create(self, customer: Customer) -> Customer:
        pass
    
    @abstractmethod
    def get_by_id(self, customer_id: str) -> Optional[Customer]:
        pass