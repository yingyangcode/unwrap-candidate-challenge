from pydantic import BaseModel, Field


class BookCreateSchema(BaseModel):
    title: str = Field(min_length=1, max_length=255)
    author: str = Field(min_length=1, max_length=100)
    isbn: str = Field(min_length=1, max_length=20)
    copies: int = Field(
        ..., gt=0, description="Number of copies must be greater than 0"
    )


class BookResponseSchema(BaseModel):
    title: str
    author: str
    isbn: str
    copies: int
    available_copies: int
