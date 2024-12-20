# Expense Tracker CLI

Expense Tracker CLI is a simple command-line interface (CLI) application for managing personal expenses. This tool allows you to add, delete, and view expenses right from your terminal, making it easy to keep track of your spending.

## Features

- **Add Expenses:** Quickly add new expenses with a description and amount.
- **Delete Expenses:** Remove expenses by their ID.
- **List Expenses:** Display all recorded expenses in a formatted table.
- **Monthly Summary:** View a summary of total expenses for a specific month or all months.

## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/under-script/ExpenseTracker.git
   ```
   
2. **Navigate to the Project Directory:**
   ```bash
   cd ExpenseTracker
   ```

3. **Install Dependencies:**
   Ensure you have Python installed. Then, install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

To start using the Expense Tracker CLI, simply run the Python script with the desired commands.

### Adding an Expense

Add a new expense by providing a description and an amount:
```bash
python main.py add "Groceries" 50
```

### Listing Expenses

List all recorded expenses:
```bash
python main.py list
```

### Deleting an Expense

Delete an expense by specifying its ID:
```bash
python main.py delete <expense_id>
```

### Viewing a Monthly Summary

View a summary of expenses for a specific month:
```bash
python main.py summary 5  # For May
```

View a summary of expenses for all months:
```bash
python main.py summary
```

## Expense File

All expenses are stored in an `expenses.json` file in the project directory. The structure of this file is managed automatically by the CLI.

### Expense Structure

Each expense has the following attributes:
- `id`: Unique identifier for the expense.
- `date`: The timestamp when the expense was added.
- `description`: A brief description of the expense.
- `amount`: The amount spent on the expense.

## Diagram

![Expense Tracker Diagram](./ExpenseTracker.svg)

## Idea Source

The idea for the Expense Tracker CLI project was inspired by [roadmap.sh's Expense Tracker project](https://roadmap.sh/projects/expense-tracker). Visit the link to see more details and learn about similar project ideas.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

1. Fork the repository.
2. Create a new branch for your feature or fix.
3. Commit your changes.
4. Push to the branch.
5. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or feedback, please contact [goldendevuz@gmail.com].

---

Happy expense tracking!