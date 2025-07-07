class LibraryException(Exception):
    def __init__(self, message: str, error_code: str, details: dict = None):
        super().__init__(message)
        self.message = message
        self.error_code = error_code
        self.details = details or {}

class BookNotFoundException(LibraryException):
    def __init__(self, isbn: str):
        super().__init__(
            message=f"Book with ISBN '{isbn}' not found",
            error_code="BOOK_NOT_FOUND",
            details={"isbn": isbn}
        )

class BookAlreadyExistsException(LibraryException):
    def __init__(self, isbn: str):
        super().__init__(
            message=f"Book with ISBN '{isbn}' already exists",
            error_code="BOOK_ALREADY_EXISTS",
            details={"isbn": isbn}
        )

class CustomerNotFoundException(LibraryException):
    def __init__(self, customer_id: str):
        super().__init__(
            message=f"Customer with ID '{customer_id}' not found",
            error_code="CUSTOMER_NOT_FOUND",
            details={"customer_id": customer_id}
        )

class CustomerAlreadyExistsException(LibraryException):
    def __init__(self, customer_id: str):
        super().__init__(
            message=f"Customer with ID '{customer_id}' already exists",
            error_code="CUSTOMER_ALREADY_EXISTS",
            details={"customer_id": customer_id}
        )

class BookNotAvailableException(LibraryException):
    def __init__(self, isbn: str):
        super().__init__(
            message="Book is not available for checkout. All copies are currently borrowed",
            error_code="BOOK_NOT_AVAILABLE",
            details={"isbn": isbn}
        )

class CustomerCheckoutLimitExceededException(LibraryException):
    def __init__(self, customer_id: str, current_count: int, max_allowed: int):
        super().__init__(
            message=f"Customer has reached maximum checkout limit of {max_allowed} books",
            error_code="CUSTOMER_CHECKOUT_LIMIT_EXCEEDED",
            details={
                "customer_id": customer_id,
                "current_checkouts": current_count,
                "max_allowed": max_allowed
            }
        )

class BookAlreadyCheckedOutException(LibraryException):
    def __init__(self, isbn: str, customer_id: str):
        super().__init__(
            message="Customer already has this book checked out",
            error_code="BOOK_ALREADY_CHECKED_OUT",
            details={"isbn": isbn, "customer_id": customer_id}
        )

class BookNotCheckedOutException(LibraryException):
    def __init__(self, isbn: str, customer_id: str):
        super().__init__(
            message="Customer does not have this book checked out",
            error_code="BOOK_NOT_CHECKED_OUT",
            details={"isbn": isbn, "customer_id": customer_id}
        )