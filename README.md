# Expense Tracker CLI

Expense Tracker CLI is a simple command-line interface (CLI) application for managing personal expenses. This tool allows you to add, delete, and view expenses right from your terminal, making it easy to keep track of your spending.

## 🔗 Project Links

- **Project Page**: [Expense Tracker project page](https://roadmap.sh/projects/expense-tracker)
- **Submission Solution**: [My Expense Tracker solution submission](https://roadmap.sh/projects/expense-tracker/solutions?u=6740b9f45434bf319a47ee77)

## 🚀 Features

- ✅ **Add Expenses**: Quickly add new expenses with a description and amount.
- ❌ **Delete Expenses**: Remove expenses by their ID.
- 📋 **List Expenses**: Display all recorded expenses in a formatted table.
- 📊 **Monthly Summary**: View a summary of total expenses for a specific month or all months.

---

## 📥 Installation

1️⃣ **Clone the Repository**:
```bash
git clone https://github.com/goldendevuz/expense-tracker.git
```

2️⃣ **Navigate to the Project Directory**:
```bash
cd expense-tracker
```

3️⃣ **Install Dependencies**:
Ensure you have Python installed. Then, install the required Python packages:
```bash
make i
```

4️⃣ **Create an Alias for CLI**:

To use the `expense-tracker` command, run:
```bash
alias expense-tracker="python main.py"
```

This will allow you to execute CLI commands using `expense-tracker` within the current terminal session.

---

## 📌 Available Commands

### 1️⃣ Add a New Expense

Use the `add` command to create a new expense:

```bash
expense-tracker add --description "Lunch" --amount 20
expense-tracker add --description "Dinner" --amount 10
```

💡 **Result**:
```bash
Expense added successfully (ID: 1)
Expense added successfully (ID: 2)
```

---

### 2️⃣ List Expenses

To display all recorded expenses:
```bash
expense-tracker list
```

📋 **Output**:
```
+----+------------+-------------+--------+
| ID |    Date    | Description | Amount |
+----+------------+-------------+--------+
| 1  | 2025-02-16 |    Lunch    |   20   |
| 2  | 2025-02-16 |    Dinner   |   10   |
+----+------------+-------------+--------+
```

---

### 3️⃣ Delete an Expense

To delete an expense by its ID:
```bash
expense-tracker delete --id 2
```

🗑️ **Result**:
```bash
Expense deleted successfully
```

---
### 5️⃣ View Monthly Summary

To view total expenses for all months:
```bash
expense-tracker summary
```

📊 **Result**:
```bash
Total expenses: $20
```

To view expenses for a specific month:
```bash
expense-tracker summary --month 8
```

📊 **Result**:
```bash
Total expenses for August: $20
```

---

## 📂 Expense File

All expenses are stored in the `expenses.json` file in the project directory.

📑 **Expense Structure**:
- `id`: Unique identifier for the expense.
- `date`: Timestamp when the expense was added.
- `description`: Brief description of the expense.
- `amount`: The amount spent on the expense.

---

## 📌 Diagram

![Expense Tracker Diagram](./ExpenseTracker.svg)

---

## 💡 Idea Source

This project was inspired by the [Expense Tracker project](https://roadmap.sh/projects/expense-tracker) from roadmap.sh. Visit the link to explore more project ideas.

---

## 🤝 Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

1. **Fork the repository.**
2. **Create a new branch**: `git checkout -b feature-branch`
3. **Commit your changes**: `git commit -m "Added new feature"`
4. **Push to the branch**: `git push origin feature-branch`
5. **Open a pull request** 🎉

---

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## ✉️ Contact

📧 For questions and feedback, contact: [goldendevuz@gmail.com](mailto:goldendevuz@gmail.com)

---

🚀 **Happy expense tracking!**