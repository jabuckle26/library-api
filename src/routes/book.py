from fastapi import APIRouter
from config.db import conn
from models.book import books

router = APIRouter(
    prefix="/books",
    tags=["books"],
    responses={404: {"description": "Not found"}},
)

@router.get("/")
async def get_all_books():
    return conn.execute(books.select()).fetchall()
