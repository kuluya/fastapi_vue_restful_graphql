from typing import List
from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def get_all_hogehoge() -> List[dict]:
    hogehoge = [
        {"id": 1, "name": "momo", "color": "SALT & PEPPER", "age": 2},
        {"id": 2, "name": "coco", "color": "DARK GREY", "age": 1.5}
    ]

    return hogehoge


@router.get('/hello')
async def hello() -> str:
    return 'hello'
