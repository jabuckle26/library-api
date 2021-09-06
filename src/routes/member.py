from config.db import conn
from fastapi import APIRouter, HTTPException
from models.member import members
from schemas.member import Member, MemberIn
from typing import List

router = APIRouter(
    prefix="/members",
    tags=["members"],
    responses={404: {"description": "Not found"}},
)


@router.get("/", response_model=List[Member])
async def get_all_members():
    return conn.execute(members.select()).fetchall()


@router.get("/get-member/{member_id}", response_model=Member)
async def get_member(member_id: int):
    query = members.select().where(member_id == members.c.id)
    returned_member = conn.execute(query)

    if returned_member is None:
        return {"data": f"No genre found with id {member_id}."}
    else:
        return returned_member.fetchone()


@router.post("/add-member", response_model=Member)
async def add_new_member(member_details: MemberIn):
    query = members.insert().values(first_name=member_details.first_name,
                                    last_name=member_details.last_name,
                                    email=member_details.email)
    last_record_id = conn.execute(query).lastrowid
    return {**member_details.dict(), "id": last_record_id}


@router.delete("/detele-member/{member_id}")
async def delete_member(member_id: int):
    query = members.delete().where(members.c.id == member_id)
    conn.execute(query)
    return {"data": f"Deleted member {member_id}."}


@router.put("/update-member/{member_id}")
async def update_member(member_id: int, member_details: Member):
    query = members.select().where(members.c.id == member_id)
    returned_members = conn.execute(query)

    if returned_members is None:
        raise HTTPException(status_code=404, detail=f"Book id #{member_id} not found")
    else:
        query = members.update().where(members.c.id == member_id).values(
            id=member_id,
            first_name=member_details.first_name,
            last_name=member_details.last_name,
            email=member_details.email
        )
        conn.execute(query)
        return member_details
