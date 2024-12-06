from fastapi import FastAPI

from .deps.database import create_db_and_tables
from .routes import transactions

app = FastAPI()

app.include_router(transactions.router, prefix="/api")


@app.on_event("startup")
def startup():
    create_db_and_tables()


@app.get("/")
def read_root():
    return {"OK": True}
