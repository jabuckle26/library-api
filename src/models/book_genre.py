from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import meta

book_genres = Table(
    'book_genre',
    meta,
    Column('id', Integer, primary_key=True),
    Column('name', String(255))
)
