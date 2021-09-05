from pydantic import BaseModel


class Book(BaseModel):
    id: int
    title: str
    author: str
    page_count: int
    book_genre: int


class BookIn(BaseModel):
    title: str
    author: str
    page_count: int
    book_genre: int
