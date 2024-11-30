from fastapi import APIRouter

router = APIRouter(prefix="/transactions", tags=["transactions"])


@router.get("/")
def get_all_data():
    return {"Transactions": "Here"}
