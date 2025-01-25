from fastapi import APIRouter

router = APIRouter()


@router.get("/hello", status_code=201)
async def hello_world():
    return "Hello World!"
