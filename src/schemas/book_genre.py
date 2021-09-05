from pydantic import BaseModel


class BookGenre(BaseModel):
    id: int
    name: str


class BookGenreIn(BaseModel):
    name: str
