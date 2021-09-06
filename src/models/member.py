from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import meta

members = Table(
    'member',
    meta,
    Column('id', Integer, primary_key=True),
    Column('first_name', String(255)),
    Column('last_name', String(255)),
    Column('email', String(255)),
)
