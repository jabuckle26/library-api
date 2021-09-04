from config.db import conn
from fastapi import APIRouter
from models.book import books
from schemas.book import Book, BookIn
from typing import List

router = APIRouter(
    prefix="/books",
    tags=["books"],
    responses={404: {"description": "Not found"}},
)


@router.get("/", response_model=List[Book])
async def get_all_books():
    return conn.execute(books.select()).fetchall()


@router.post("/add-book", response_model=Book)
async def add_new_book(book: BookIn):
    query = books.insert().values(title=book.title,
                                  author=book.author,
                                  page_count=book.page_count)
    last_record_id = conn.execute(query).lastrowid
    return {**book.dict(), "id": last_record_id}
