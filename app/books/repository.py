from typing import Optional
from app.books.interfaces import BookRepositoryInterface
from app.storage.memory_store import MemoryStore
from app.books.models import Book
from app.exceptions import BookAlreadyExistsException


class BookRepository(BookRepositoryInterface):
    def __init__(self, memory_store: MemoryStore):
        self.store = memory_store
    
    def create(self, book: Book) -> Book:
        if book.isbn in self.store._books:
            raise BookAlreadyExistsException(book.isbn)
        
        self.store._books[book.isbn] = book
        return book
    
    def get_by_isbn(self, isbn: str) -> Optional[Book]:
        return self.store._books.get(isbn)
    
    def get_available_copies(self, isbn: str) -> int:
        book = self.store._books.get(isbn)
        if not book:
            return 0
        
        active_checkouts = sum(1 for checkout in self.store._checkouts 
                             if checkout.isbn == isbn and checkout.return_date is None)
        return book.copies - active_checkouts