from typing import Dict, List, Optional
from app.books.models import Book
from app.customers.models import Customer
from app.checkouts.models import Checkout


class MemoryStore:
    def __init__(self):
        self._books: Dict[str, Book] = {}
        self._customers: Dict[str, Customer] = {}
        self._checkouts: List[Checkout] = []
        self._counter = 0
    
    def reset(self):
        self._books.clear()
        self._customers.clear()
        self._checkouts.clear()
        self._counter = 0


# Global instance
memory_store = MemoryStore()