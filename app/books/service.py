from app.books.interfaces import BookRepositoryInterface
from app.books.models import Book, BookWithAvailability
from app.exceptions import BookNotFoundException


class BookService:
    def __init__(self, book_repo: BookRepositoryInterface):
        self.book_repo = book_repo
    
    def create_book(self, isbn: str, title: str, author: str, copies: int) -> Book:
       
        book = Book(
            isbn=isbn,
            title=title,
            author=author,
            copies=copies,
        )
        
        result = self.book_repo.create(book)
        return result
    
    def get_book_by_isbn(self, isbn: str) -> BookWithAvailability:
        book = self.book_repo.get_by_isbn(isbn)
        if not book:
            raise BookNotFoundException(isbn)
        
        available_copies = self.book_repo.get_available_copies(isbn)
        return BookWithAvailability(**book.model_dump(), available_copies=available_copies)