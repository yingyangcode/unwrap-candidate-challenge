from fastapi import HTTPException, Request
from fastapi.responses import JSONResponse
from app.exceptions import LibraryException


async def library_exception_handler(request: Request, exc: LibraryException) -> JSONResponse:
    """Global exception handler for LibraryException"""
    
    # Map specific error codes to HTTP status codes
    status_code_map = {
        "BOOK_NOT_FOUND": 404,
        "CUSTOMER_NOT_FOUND": 404,
        "BOOK_ALREADY_EXISTS": 409,
        "CUSTOMER_ALREADY_EXISTS": 409,
        "BOOK_NOT_AVAILABLE": 400,
        "CUSTOMER_CHECKOUT_LIMIT_EXCEEDED": 400,
        "BOOK_ALREADY_CHECKED_OUT": 400,
        "BOOK_NOT_CHECKED_OUT": 400,
        "UNAUTHORIZED_RETURN": 400,
    }
    
    status_code = status_code_map.get(exc.error_code, 400)
    
    return JSONResponse(
        status_code=status_code,
        content={
            "error": exc.error_code,
            "message": exc.message,
            "details": exc.details
        }
    )