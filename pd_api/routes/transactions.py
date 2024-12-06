from fastapi import APIRouter
from sqlmodel import select

from ..models.transaction import Transaction
from ..deps.database import DBSession

router = APIRouter(prefix="/transactions", tags=["transactions"])


@router.get("/")
def get_all_data(*, db: DBSession) -> list[Transaction]:
    data = db.exec(select(Transaction)).all()
    return data
