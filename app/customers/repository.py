from typing import Optional
from app.customers.interfaces import CustomerRepositoryInterface
from app.storage.memory_store import MemoryStore
from app.customers.models import Customer
from app.exceptions import CustomerAlreadyExistsException


class CustomerRepository(CustomerRepositoryInterface):
    def __init__(self, memory_store: MemoryStore):
        self.store = memory_store
    
    def create(self, customer: Customer) -> Customer:
        if customer.customer_id in self.store._customers:
            raise CustomerAlreadyExistsException(customer.customer_id)
        
        self.store._customers[customer.customer_id] = customer
        return customer
    
    def get_by_id(self, customer_id: str) -> Optional[Customer]:
        return self.store._customers.get(customer_id)