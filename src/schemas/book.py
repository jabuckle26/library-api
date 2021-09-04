from pydantic import BaseModel


class Book(BaseModel):
    id: int
    title: str
    page_count: int
