from pydantic import BaseModel
from datetime import datetime


class BorrowedBooks(BaseModel):
    id: int
    book_id: int
    member_id: int
    withdraw_date: datetime
    due_date: datetime
    is_overdue: bool
    is_returned: bool
    returned_date: datetime


class BorrowedBooksIn(BaseModel):
    book_id: int
    member_id: int
    withdraw_date: datetime
    due_date: datetime
    is_overdue: bool
    is_returned: bool
    returned_date: datetime
