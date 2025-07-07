from pydantic import BaseModel


class Book(BaseModel):
    title: str
    author: str
    isbn: str
    copies: int

    class Config:
        frozen = True
    


class BookWithAvailability(BaseModel):
    title: str
    author: str
    isbn: str
    copies: int
    available_copies: int