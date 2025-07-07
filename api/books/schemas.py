from pydantic import BaseModel
from typing import Optional


class BookCreateSchema(BaseModel):
    title: str
    author: str
    isbn: str
    copies: int


class BookResponseSchema(BaseModel):
    title: str
    author: str
    isbn: str
    copies: int
    available_copies: int