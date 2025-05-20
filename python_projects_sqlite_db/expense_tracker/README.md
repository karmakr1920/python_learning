# Expense Tracker CLI (Python + SQLite)

A simple command-line expense tracker that lets you manage, search, and export your personal expenses. Built with **Python** and **SQLite**, it includes recurring expense support, CSV export, monthly summaries, and password protection.

---

## Features

- ✅ Add, update, delete, and search expenses
- 📆 Date-based sorting and filtering
- 🔁 Recurring expense tagging (`weekly`, `monthly`, etc.)
- 📊 Monthly summary with total expenses per month
- 📈 Category-wise expense breakdown
- 🔐 Password-protected access
- 💾 Export all data to CSV

---

## Table Structure

SQLite table: `expenses`

| Column     | Type    | Description                    |
|------------|---------|--------------------------------|
| id         | INTEGER | Auto-incremented expense ID    |
| amount     | REAL    | Amount spent                   |
| category   | TEXT    | Category of the expense        |
| date       | TEXT    | Date in `YYYY-MM-DD` format    |
| note       | TEXT    | Optional note for the entry    |
| recurring  | TEXT    | Recurrence: `monthly`, etc.    |

---

## Setup Instructions

1. **Clone the repository**:

```bash
git clone https://github.com/karmakr1920/python_learning.git
cd python_projects_sqlite_db/expense_tracker
````

2. **Run the program**:

```bash
python expense_tracker.py
```

3. **Enter password** (default is `admin123` — change this in the script for security):

```
Enter password: admin123
```

---

## How to Use

### Main Menu

```
1. List expenses
2. Add expense
3. Update expense
4. Delete expense
5. Search by keyword
6. Show monthly summary
7. Show category breakdown
8. Export to CSV
9. Exit
```

### Sample Entry

```text
Amount: 125.50
Category: Groceries
Date: 2024-05-01
Note: Monthly food shopping
Recurring: monthly
```

---

## Export to CSV

Outputs `expenses.csv` in the project directory, containing all records in the database.

---

## Dependencies

* Python 3.6+
* Built-in modules: `sqlite3`, `csv`, `datetime`, `getpass`

No third-party packages required.

---

## License

This project is licensed under the MIT License. Feel free to use, modify, and distribute it.

---

## Author

**Your Name**
GitHub: https://github.com/karmakr1920