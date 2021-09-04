from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import meta

books = Table(
    'book',
    meta,
    Column('id', Integer, primary_key=True),
    Column('title', String(255)),
    Column('author', String(255))
)
