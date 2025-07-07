from typing import List, Optional
from datetime import datetime
from app.checkouts.interfaces import CheckoutRepositoryInterface
from app.storage.memory_store import MemoryStore
from app.checkouts.models import Checkout


class CheckoutRepository(CheckoutRepositoryInterface):
    def __init__(self, memory_store: MemoryStore):
        self.store = memory_store
    
    def create_checkout(self, isbn: str, customer_id: str, due_date: str) -> Checkout:
        self.store._counter += 1
        
        new_checkout = Checkout(
            checkout_id=f'CKO{self.store._counter:06d}',
            isbn=isbn,
            customer_id=customer_id,
            checkout_date=datetime.now().strftime('%Y-%m-%d'),
            due_date=due_date,
            return_date=None
        )
        
        self.store._checkouts.append(new_checkout)
        return new_checkout
    
    def get_active_by_customer(self, customer_id: str) -> List[Checkout]:
        return [c for c in self.store._checkouts 
                if c.customer_id == customer_id and c.return_date is None]
    
    def mark_returned(self, isbn: str, customer_id: str) -> Optional[Checkout]:
        for i, checkout in enumerate(self.store._checkouts):
            if (checkout.isbn == isbn and 
                checkout.customer_id == customer_id and 
                checkout.return_date is None):
                # Since Pydantic models are frozen, create a new one with return_date
                returned_checkout = checkout.model_copy(update={
                    'return_date': datetime.now().strftime('%Y-%m-%d')
                })
                self.store._checkouts[i] = returned_checkout
                return returned_checkout
        return None
    
    def get_active_checkout(self, isbn: str, customer_id: str) -> Optional[Checkout]:
        for checkout in self.store._checkouts:
            if (checkout.isbn == isbn and 
                checkout.customer_id == customer_id and 
                checkout.return_date is None):
                return checkout
        return None