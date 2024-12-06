import uuid
from sqlmodel import SQLModel, Field
from datetime import datetime, timezone


class Transaction(SQLModel, table=True):
    id: str = Field(primary_key=True, default_factory=lambda: uuid.uuid4().hex)
    amount: int
    currency_rate: float
    description: str
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(
        default_factory=datetime.now,
        sa_column_kwargs={"onupdate": datetime.now},
    )
