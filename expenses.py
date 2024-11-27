from datetime import datetime

from models import Expense
from storage.json_handler import JsonHandler


class ExpenseManager:
    def __init__(self, storage: JsonHandler) -> None:
        self.storage = storage

    def add_expense(self, description: str, amount: int) -> Expense:
        expenses: dict = self.storage.read()
        expense_id: int = len(expenses) + 1
        expense: Expense = Expense(id=expense_id, description=description, amount=amount, date=str(datetime.today().date()))
        self.storage.write(expense_id, expense.model_dump())
        return expense

    def update_description(self, expense_id: int, description: str) -> bool:
        expenses: dict = self.storage.read()
        key: str = str(expense_id)
        if key in expenses:
            expenses[key]["description"]: str = description
            expenses[key]["updatedAt"]: str = str(datetime.now())
            self.storage.write(expense_id, expenses[key])
            return True
        return False

    def delete_expense(self, expense_id: int) -> bool:
        expenses: dict = self.storage.read()
        key: str = str(expense_id)
        if key in expenses:
            self.storage.delete(expense_id)
            return True
        return False

    def check_availability(self, description: str = "", expense_id: int = 0) -> bool:
        expenses: dict = self.storage.read()
        if expense_id:
            return str(expense_id) in expenses
        return any(expense['description'] == description for expense in expenses.values())

    def check_exact(self, expense_id: int, description: str) -> bool:
        expenses: dict = self.storage.read()
        return expenses[str(expense_id)]['description'] == description
        # return self.check_availability(description)

    def check_status(self, expense_id: int) -> bool:
        expenses: dict = self.storage.read()
        return expenses[str(expense_id)]['status']

    def update_status(self, expense_id: int) -> bool:
        expenses: dict = self.storage.read()
        key = str(expense_id)
        if key in expenses:
            expenses[key]["updatedAt"]: str = str(datetime.now())
            self.storage.write(expense_id, expenses[key])
            return True
        return False

    def list_expenses(self) -> dict:
        expenses: dict = self.storage.read()
        return expenses
