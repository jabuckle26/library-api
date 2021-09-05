from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import meta

books = Table(
    'book',
    meta,
    Column('id', Integer, primary_key=True),
    Column('title', String(255)),
    Column('author', String(255)),
    Column('page_count', Integer),
    Column('book_genre', Integer, ForeignKey("book_genre.id")),
)
