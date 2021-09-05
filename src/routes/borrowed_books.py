from config.db import conn
from fastapi import APIRouter
from models.borrowed_books import borrowed_books
from schemas.borrowed_books import BorrowedBooks, BorrowedBooksIn
from typing import List

router = APIRouter(
    prefix="/borrowed-books",
    tags=["borrowed-books"],
    responses={404: {"description": "Not found"}},
)


@router.get("/", response_model=List[BorrowedBooks])
async def get_all_borrowed_books():
    return conn.execute(borrowed_books.select()).fetchall()


@router.get("/get-borrowed_books/{borrowed_books_id}", response_model=BorrowedBooks)
async def get_borrowed_books(borrowed_books_id: int):
    query = borrowed_books.select().where(borrowed_books_id == borrowed_books.c.id)
    returned_borrowed_books = conn.execute(query)

    if returned_borrowed_books is None:
        return {"data": f"No genre found with id {borrowed_books_id}."}
    else:
        return returned_borrowed_books.fetchone()


@router.post("/add-borrowed_books", response_model=BorrowedBooks)
async def add_new_borrowed_books(borrowed_books_details: BorrowedBooksIn):
    query = borrowed_books.insert().values(book_id=borrowed_books_details.book_id,
                                           member_id=borrowed_books_details.member_id,
                                           withdraw_date=borrowed_books_details.withdraw_date,
                                           due_date=borrowed_books_details.due_date,
                                           is_overdue=borrowed_books_details.is_overdue,
                                           is_returned=borrowed_books_details.is_returned,
                                           returned_date=borrowed_books_details.returned_date
                                           )
    last_record_id = conn.execute(query).lastrowid
    return {**borrowed_books_details.dict(), "id": last_record_id}


@router.delete("/detele-borrowed_books/{borrowed_books_id}")
async def delete_borrowed_books(borrowed_books_id: int):
    query = borrowed_books.delete().where(borrowed_books.c.id == borrowed_books_id)
    conn.execute(query)
    return {"data": f"Deleted borrowed_books {borrowed_books_id}."}


@router.put("/update-borrowed_books/{borrowed_books_id}")
async def update_borrowed_books(borrowed_books_id: int, borrowed_books_details: BorrowedBooks):
    query = borrowed_books.update().where(borrowed_books.c.id == borrowed_books_id).values(
        id=borrowed_books_id,
        book_id=borrowed_books_details.book_id,
        member_id=borrowed_books_details.member_id,
        withdraw_date=borrowed_books_details.withdraw_date,
        due_date=borrowed_books_details.due_date,
        is_overdue=borrowed_books_details.is_overdue,
        is_returned=borrowed_books_details.is_returned,
        returned_date=borrowed_books_details.returned_date
    )
    conn.execute(query)
    return borrowed_books_details
