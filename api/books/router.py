from fastapi import APIRouter
from api.books.schemas import BookCreateSchema, BookResponseSchema
from app.books.service import BookService
from app.books.repository import BookRepository
from app.storage.memory_store import memory_store

router = APIRouter(tags=["books"])


@router.post("/books", response_model=BookResponseSchema, status_code=201)
def create_book(request: BookCreateSchema):
    book_repo = BookRepository(memory_store)
    book_service = BookService(book_repo)
    book_result = book_service.create_book(
        isbn=request.isbn,
        title=request.title,
        author=request.author,
        copies=request.copies
    )
    available_copies = book_repo.get_available_copies(book_result.isbn)
    return BookResponseSchema(**book_result.model_dump(), available_copies=available_copies)


@router.get("/books/{isbn}", response_model=BookResponseSchema)
def get_book(isbn: str):
    book_repo = BookRepository(memory_store)
    book_service = BookService(book_repo)
    book_result = book_service.get_book_by_isbn(isbn)
    return BookResponseSchema(**book_result.model_dump())