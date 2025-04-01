import argparse
from datetime import datetime, date
from typing import List, Optional, Union, Any, Tuple
from colorama import Fore, Style, init
from enums import Action
from storage.json_handler import JsonHandler
from expenses import ExpenseManager
from prettytable import PrettyTable

table = PrettyTable()

# Initialize Colorama
init(autoreset=True)

parser = argparse.ArgumentParser()
parser.add_argument(
    "action",
    choices=[action.value for action in Action],
    help="The action to perform (add, delete, update, list)",
)
parser.add_argument(
    "--description", type=str,
    help="The description of the expense",
)
parser.add_argument(
    "--amount", type=int,
    help="The amount of the expense",
)
parser.add_argument(
    "--id", type=int,
    help="The id of the expense",
)
parser.add_argument(
    "--month", type=int,
    help="The month of the expense",
)
args = parser.parse_args()

storage: JsonHandler = JsonHandler()
expense_manager: ExpenseManager = ExpenseManager(storage)

def main() -> str | PrettyTable:
    if args.action == Action.ADD:
        if 1 == Action:
            return f"{Fore.RED}Error: The 'add' action requires exactly one argument: the description.{Style.RESET_ALL}"
        else:
            description, amount = args.description, args.amount
            if expense_manager.check_availability(description):
                return f"{Fore.YELLOW}Expense already added{Style.RESET_ALL}"
            else:
                expense = expense_manager.add_expense(description=description, amount=amount)
                return f"{Fore.GREEN}Expense added successfully (ID: {expense.id}){Style.RESET_ALL}"
    elif args.action == Action.DELETE:
        if 1 == Action:
            return f"{Fore.RED}Error: The 'delete' action requires exactly one argument: the ID.{Style.RESET_ALL}"
        else:
            try:
                expense_id: int = int(args.id)
                if expense_manager.check_availability(expense_id=expense_id):
                    expense_manager.delete_expense(expense_id)
                    return f"{Fore.GREEN}Expense with ID {expense_id} deleted.{Style.RESET_ALL}"
                else:
                    return f"{Fore.RED}Expense doesn't exist{Style.RESET_ALL}"
            except ValueError:
                return f"{Fore.RED}Error: The expense ID must be an integer.{Style.RESET_ALL}"
    elif args.action == Action.LIST:
        expenses: dict = expense_manager.list_expenses()
        if expenses:
            table.field_names = ["ID", "Date", "Description", "Amount"]
            for expense in expenses.values():
                table.add_row([
                    expense["id"],
                    expense["date"],
                    expense["description"],
                    expense["amount"],
                ])
            if table.rows:
                return table
        return "No expenses found."
    elif args.action == Action.SUMMARY:
        expenses: dict = expense_manager.list_expenses()
        if expenses:
            if args.month is not None:
                if args.month in range(1, 12):
                    summary: int = sum(expense["amount"] for expense in expenses.values() if date.fromisoformat(expense["date"]).month == args.month)
                else:
                    return f"{Fore.RED}Error: Invalid month{Style.RESET_ALL}"
            else:
                summary: int = sum(expense["amount"] for expense in expenses.values())
            return f"Total expenses: ${summary}"
        return "No expenses found."
    else:
        return f"{Fore.RED}Invalid action.{Style.RESET_ALL}"


if __name__ == "__main__":
    print(main())
