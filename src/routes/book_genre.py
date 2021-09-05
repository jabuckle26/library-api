from config.db import conn
from fastapi import APIRouter
from models.book_genre import book_genres
from schemas.book_genre import BookGenre, BookGenreIn
from typing import List

router = APIRouter(
    prefix="/book-geres",
    tags=["book-genres"],
    responses={404: {"description": "Not found"}},
)


@router.get("/", response_model=List[BookGenre])
async def get_all_book_genres():
    return conn.execute(book_genres.select()).fetchall()


@router.get("/get-book-genre/{book_genre_id}", response_model=BookGenre)
async def get_book_genre(book_genre_id: int):
    query = book_genres.select().where(book_genre_id == book_genres.c.id)
    returned_book_genre = conn.execute(query)

    if returned_book_genre is None:
        return {"data": f"No genre found with id {book_genre_id}."}
    else:
        return returned_book_genre.fetchone()


@router.post("/add-book-genre", response_model=BookGenre)
async def add_new_genre(book_genre: BookGenreIn):
    query = book_genres.insert().values(name=book_genre.name)
    last_record_id = conn.execute(query).lastrowid
    return {**book_genre.dict(), "id": last_record_id}


@router.delete("/detele-book-genre/{book_genre_id}")
async def delete_book_genre(book_genre_id: int):
    query = book_genres.delete().where(book_genres.c.id == book_genre_id)
    conn.execute(query)
    return {"data": f"Deleted book {book_genre_id}."}


@router.put("/update-book-genre/{book_genre_id}")
async def update_book(book_genre_id: int, book_genre_details: BookGenre):
    query = book_genres.update().where(book_genres.c.id == book_genre_id).values(
        id=book_genre_id,
        name=book_genre_details.name
    )
    conn.execute(query)
    return book_genre_details
