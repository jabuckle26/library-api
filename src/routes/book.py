from config.db import conn
from fastapi import APIRouter, HTTPException
from models.book import books
from schemas.book import Book, BookIn
from typing import List, Optional

router = APIRouter(
    prefix="/books",
    tags=["books"],
    responses={404: {"description": "Not found"}},
)


@router.get("/", response_model=List[Book])
async def get_all_books(search_term: Optional[str] = None):
    if search_term:
        print(f'Got.....{search_term}')
        query = books.select().filter(books.c.title.contains(search_term))
        queried_book = conn.execute(query)
        returned_books = queried_book.fetchall()

        if len(returned_books) == 0:
            raise HTTPException(status_code=404, detail=f"No books found matching query.")
        else:
            return returned_books
    else:
        return conn.execute(books.select()).fetchall()


@router.get("/get-book/{book_id}", response_model=Book)
async def get_book(book_id: int):
    query = books.select().where(book_id == books.c.id)
    queried_book = conn.execute(query)
    returned_book = queried_book.fetchone()

    if returned_book is None:
        raise HTTPException(status_code=404, detail=f"Book id #{book_id} not found")
    else:
        return returned_book


@router.post("/add-book", response_model=Book)
async def add_new_book(book_details: BookIn):
    query = books.insert().values(title=book_details.title,
                                  author=book_details.author,
                                  page_count=book_details.page_count,
                                  book_genre=book_details.book_genre)
    last_record_id = conn.execute(query).lastrowid
    return {**book_details.dict(), "id": last_record_id}


@router.delete("/detele-book/{book_id}")
async def delete_book(book_id: int):
    query = books.delete().where(books.c.id == book_id)
    conn.execute(query)
    return {"data": f"Deleted book {book_id}."}


@router.put("/update-book/{book_id}")
async def update_book(book_id: int, book_details: Book):
    query = books.select().where(book_id == books.c.id)
    returned_book = conn.execute(query)

    if returned_book.fetchone() is None:
        raise HTTPException(status_code=404, detail=f"Book id #{book_id} not found")
    else:
        query = books.update().where(books.c.id == book_id).values(
            id=book_id,
            title=book_details.title,
            author=book_details.author,
            page_count=book_details.page_count,
            book_genre=book_details.book_genre
        )
        conn.execute(query)
        return book_details
