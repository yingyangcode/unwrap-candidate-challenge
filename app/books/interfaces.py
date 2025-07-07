from abc import ABC, abstractmethod
from typing import Optional
from app.books.models import Book


class BookRepositoryInterface(ABC):
    @abstractmethod
    def create(self, book: Book) -> Book:
        pass
    
    @abstractmethod
    def get_by_isbn(self, isbn: str) -> Optional[Book]:
        pass
    
    @abstractmethod
    def get_available_copies(self, isbn: str) -> int:
        pass