from pydantic import BaseModel


class Expense(BaseModel):
    id: int
    date: str
    description: str
    amount: int
