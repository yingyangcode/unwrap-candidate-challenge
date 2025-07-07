from datetime import datetime
from typing import List
from app.checkouts.interfaces import CheckoutRepositoryInterface
from app.books.interfaces import BookRepositoryInterface
from app.customers.interfaces import CustomerRepositoryInterface
from app.checkouts.models import Checkout, CheckoutWithTitle
from app.config import LibraryConfig
from app.exceptions import (
    BookNotFoundException, 
    CustomerNotFoundException, 
    BookNotAvailableException,
    CustomerCheckoutLimitExceededException,
    BookAlreadyCheckedOutException,
    BookNotCheckedOutException
)


class CheckoutService:
    def __init__(self, 
                 checkout_repo: CheckoutRepositoryInterface,
                 book_repo: BookRepositoryInterface,
                 customer_repo: CustomerRepositoryInterface):
        self.checkout_repo = checkout_repo
        self.book_repo = book_repo
        self.customer_repo = customer_repo
    
    def checkout_book(self, isbn: str, customer_id: str, due_date: str) -> CheckoutWithTitle:
        
        book = self.book_repo.get_by_isbn(isbn)
        if not book:
            raise BookNotFoundException(isbn)
        
        customer = self.customer_repo.get_by_id(customer_id)
        if not customer:
            raise CustomerNotFoundException(customer_id)
        
        existing_checkout = self.checkout_repo.get_active_checkout(isbn, customer_id)
        if existing_checkout:
            raise BookAlreadyCheckedOutException(isbn, customer_id)
        
        # Check customer checkout limit
        active_checkouts = self.checkout_repo.get_active_by_customer(customer_id)
        max_checkouts = LibraryConfig.MAX_CHECKOUTS_PER_CUSTOMER
        if len(active_checkouts) >= max_checkouts:
            raise CustomerCheckoutLimitExceededException(customer_id, len(active_checkouts), max_checkouts)
        
        # Check book availability
        available_copies = self.book_repo.get_available_copies(isbn)
        if available_copies <= 0:
            raise BookNotAvailableException(isbn)
        
        checkout = self.checkout_repo.create_checkout(
            isbn=isbn,
            customer_id=customer_id,
            due_date=due_date
        )
        return CheckoutWithTitle(
            **checkout.model_dump(),
            title=book.title
        )
    
    def return_book(self, isbn: str, customer_id: str) -> Checkout:
        
        book = self.book_repo.get_by_isbn(isbn)
        if not book:
            raise BookNotFoundException(isbn)
        
        customer = self.customer_repo.get_by_id(customer_id)
        if not customer:
            raise CustomerNotFoundException(customer_id)
        
        # Check if customer has this book checked out
        active_checkout = self.checkout_repo.get_active_checkout(isbn, customer_id)
        if not active_checkout:
            raise BookNotCheckedOutException(isbn, customer_id)
        
        # Mark as returned
        returned_checkout = self.checkout_repo.mark_returned(isbn, customer_id)
        if not returned_checkout:
            raise BookNotCheckedOutException(isbn, customer_id)
        
        return returned_checkout
    
    def get_customer_checkouts(self, customer_id: str) -> List[Checkout]:
        customer = self.customer_repo.get_by_id(customer_id)
        if not customer:
            raise CustomerNotFoundException(customer_id)
        
        active_checkouts = self.checkout_repo.get_active_by_customer(customer_id)
        return active_checkouts