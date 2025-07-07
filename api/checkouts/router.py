from fastapi import APIRouter
from typing import List
from api.checkouts.schemas import (
    CheckoutCreateSchema, CheckoutResponseSchema,
    ReturnCreateSchema, ReturnResponseSchema,
    CustomerBooksSchema
)
from app.checkouts.service import CheckoutService
from app.checkouts.repository import CheckoutRepository
from app.books.repository import BookRepository
from app.customers.repository import CustomerRepository
from app.storage.memory_store import memory_store

router = APIRouter(tags=["checkouts"])


@router.post("/checkouts", response_model=CheckoutResponseSchema, status_code=201)
def checkout_book(request: CheckoutCreateSchema):
    checkout_repo = CheckoutRepository(memory_store)
    book_repo = BookRepository(memory_store)
    customer_repo = CustomerRepository(memory_store)
    checkout_service = CheckoutService(checkout_repo, book_repo, customer_repo)
    checkout_result = checkout_service.checkout_book(
        isbn=request.isbn,
        customer_id=request.customer_id,
        due_date=request.due_date
    )
    return CheckoutResponseSchema(**checkout_result.model_dump())


@router.post("/returns", response_model=ReturnResponseSchema)
def return_book(request: ReturnCreateSchema):
    checkout_repo = CheckoutRepository(memory_store)
    book_repo = BookRepository(memory_store)
    customer_repo = CustomerRepository(memory_store)
    checkout_service = CheckoutService(checkout_repo, book_repo, customer_repo)
    returned_checkout = checkout_service.return_book(
        isbn=request.isbn,
        customer_id=request.customer_id
    )
    return ReturnResponseSchema(
        message="Book returned successfully",
        isbn=returned_checkout.isbn,
        customer_id=returned_checkout.customer_id,
        return_date=returned_checkout.return_date
    )


@router.get("/customers/{customer_id}/books", response_model=List[CustomerBooksSchema])
def get_customer_books(customer_id: str):
    checkout_repo = CheckoutRepository(memory_store)
    book_repo = BookRepository(memory_store)
    customer_repo = CustomerRepository(memory_store)
    checkout_service = CheckoutService(checkout_repo, book_repo, customer_repo)
    checkouts = checkout_service.get_customer_checkouts(customer_id)
    
    result = []
    for checkout in checkouts:
        book = book_repo.get_by_isbn(checkout.isbn)
        
        checkout_response = CustomerBooksSchema(
            isbn=checkout.isbn,
            title=book.title if book else 'Unknown',
            author=book.author if book else 'Unknown',
            checkout_date=checkout.checkout_date,
            due_date=checkout.due_date
        )
        result.append(checkout_response)
    
    return result