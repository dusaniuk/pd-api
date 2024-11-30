from fastapi import FastAPI

from pd_api.routes import transactions

app = FastAPI()

app.include_router(transactions.router)


@app.get("/")
def read_root():
    return {"OK": True}
