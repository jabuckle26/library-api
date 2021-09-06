from pydantic import BaseModel


class Member(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: str


class MemberIn(BaseModel):
    first_name: str
    last_name: str
    email: str
