# Expense Tracker CLI

Expense Tracker CLI is a command-line application built in Python to help you manage expenses efficiently. It allows you to add, update, delete, and track expenses, while saving the expenses in a JSON file for persistence.

## Project Links

- **Project Page**: Visit the [Expense Tracker project page](https://roadmap.sh/projects/expense-tracker) for more information.
- **Submission Solution**: View my [Expense Tracker solution submission](https://roadmap.sh/projects/expense-tracker/solutions?u=6740b9f45434bf319a47ee77).

## Features

- Add new expenses
- Update expense descriptions
- Delete expenses
- Mark expenses as in-progress or done
- List all expenses or filter expenses by status (todo, in-progress, done)
- Expenses are stored in a `expenses.json` file

## Installation

### Prerequisites

- **Python**: Make sure you have Node.js installed. You can download it [here](https://www.python.org/downloads/).

### Steps

1. **Clone the repository**:

   ```bash
   git clone https://github.com/goldendevuz/expense-tracker.git
   cd expense-tracker
   ```

2. **Install dependencies**:

   ```bash
   make i
   ```

4. **Link the CLI globally**:

   To use the `expense-cli` command globally, run:

   ```bash
   make link
   ```

   This will make the `expense-cli` command available system-wide.

## Usage

Once you've linked the CLI, you can use the `expense-cli` command to interact with the Expense Tracker.

### Available Commands

#### 1. Add a New Expense

Use the `add` command to create a new expense.

```bash
expense-cli add "Expense description"
```

**Example**:

```bash
expense-cli add "Finish the project report"
```

#### 2. Update a Expense

Use the `update` command to modify the description of an existing expense by its ID.

```bash
expense-cli update <expense_id> "Updated description"
```

**Example**:

```bash
expense-cli update 1 "Finish the project report and submit"
```

#### 3. Delete a Expense

Use the `delete` command to remove a expense by its ID.

```bash
expense-cli delete <expense_id>
```

**Example**:

```bash
expense-cli delete 1
```

#### 4. Mark a Expense as In Progress

Use the `mark-in-progress` command to update the status of a expense to `in-progress`.

```bash
expense-cli mark-in-progress <expense_id>
```

**Example**:

```bash
expense-cli mark-in-progress 1
```

#### 5. Mark a Expense as Done

Use the `mark-done` command to update the status of a expense to `done`.

```bash
expense-cli mark-done <expense_id>
```

**Example**:

```bash
expense-cli mark-done 1
```

#### 6. List All Expenses

Use the `list` command to view all expenses.

```bash
expense-cli list
```

**Example**:

```bash
expense-cli list
```

#### 7. List Expenses by Status

You can filter expenses by their status using the `list` command followed by the status (`todo`, `in-progress`, or `done`).

```bash
expense-cli list <status>
```

**Examples**:

- List all expenses marked as `done`:

  ```bash
  expense-cli list done
  ```

- List all expenses marked as `in-progress`:

  ```bash
  expense-cli list in-progress
  ```

- List all expenses that are yet to be done:
  ```bash
  expense-cli list todo
  ```

### Expense Properties

Each expense has the following properties:

- **id**: A unique identifier for the expense.
- **description**: The description of the expense.
- **status**: The status of the expense (`todo`, `in-progress`, `done`).
- **createdAt**: The date and time when the expense was created.
- **updatedAt**: The date and time when the expense was last updated.

### Example JSON Structure

Expenses are stored in a JSON file located in the project directory as `expenses.json`. Here's an example of how expenses are stored:

```json
[
  {
    "id": 1,
    "description": "Finish the project report",
    "status": "in-progress",
    "createdAt": "2024-09-10T12:34:56.789Z",
    "updatedAt": "2024-09-10T14:23:44.456Z"
  },
  {
    "id": 2,
    "description": "Review the design documents",
    "status": "done",
    "createdAt": "2024-09-10T13:45:12.123Z",
    "updatedAt": "2024-09-10T15:11:22.987Z"
  }
]
```

## Development

### Running the CLI Locally

To test the CLI without linking globally, you can run it using:

```bash
python main.py <command> [args]
```

### Testing

Manually test the application by running the various commands listed above. Be sure to check the `expenses.json` file to ensure expenses are saved correctly.

## Contributing

If you'd like to contribute, please fork the repository and use a feature branch. Pull requests are always welcome.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.