from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def api_test():
    return {"message": "Welcome to the API"}
