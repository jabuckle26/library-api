from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, DateTime, Boolean
from config.db import meta

borrowed_books = Table(
    'borrowed_books',
    meta,
    Column('id', Integer, primary_key=True),
    Column('book_id', Integer, ForeignKey("book.id")),
    Column('member_id', Integer, ForeignKey("member.id")),
    Column('withdraw_date', DateTime),
    Column('due_date', DateTime),
    Column('is_returned', Boolean),
    Column('returned_date', DateTime)
)
