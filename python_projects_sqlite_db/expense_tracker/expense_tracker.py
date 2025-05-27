import sqlite3
import csv
import getpass
from datetime import datetime

# --- CONFIGURABLE PASSWORD ---
MASTER_PASSWORD = "admin123"

# --- DATABASE SETUP ---
conn = sqlite3.connect('expense_tracker.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS expenses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        amount REAL NOT NULL,
        category TEXT NOT NULL,
        date TEXT NOT NULL,
        note TEXT,
        recurring TEXT
    )
''')

# --- CORE FUNCTIONS ---
def list_expenses():
    cursor.execute("SELECT * FROM expenses ORDER BY date DESC")
    expenses = cursor.fetchall()
    if not expenses:
        print("No expenses found.")
        return []
    print("\nList of Expenses:")
    for expense in expenses:
        try:
            readable_date = datetime.strptime(expense[3], '%Y-%m-%d').strftime('%d %b %Y')
        except ValueError:
            readable_date = expense[3]
        print(f"ID: {expense[0]} | Amount: {expense[1]} | Category: {expense[2]} | Date: {readable_date} | Note: {expense[4]} | Recurring: {expense[5]}")
    return expenses


def add_expense(amount, category, date, note,recurring):
    # Check for duplicate
    cursor.execute(
        "SELECT * FROM expenses WHERE amount = ? AND category = ? AND date = ? AND note = ? AND recurring = ?",
        (amount, category, date, note,recurring)
    )
    if cursor.fetchone():
        print("Duplicate expense found. Expense not added.")
        return
    cursor.execute(
        "INSERT INTO expenses(amount, category, date, note,recurring) VALUES (?, ?, ?, ?,?)",
        (amount, category, date, note,recurring)
    )
    conn.commit()
    print("Expense added successfully.")


def update_expense(expense_id, amount, category, date, note, recurring):
    cursor.execute("SELECT * FROM expenses WHERE id = ?", (expense_id,))
    if cursor.fetchone() is None:
        print("Expense ID not found.")
        return
    cursor.execute("UPDATE expenses SET amount = ?, category = ?, date = ?, note = ?, recurring = ? WHERE id = ?",
                   (amount, category, date, note, recurring, expense_id))
    conn.commit()
    print("Expense updated successfully.")

def delete_expense(expense_id):
    cursor.execute("SELECT * FROM expenses WHERE id = ?", (expense_id,))
    if cursor.fetchone() is None:
        print("Expense ID not found.")
        return
    cursor.execute("DELETE FROM expenses WHERE id = ?", (expense_id,))
    conn.commit()
    print("Expense deleted successfully.")

def search_expense_by_keyword(keyword):
    query = '''
        SELECT id, amount, category, date, note, recurring
        FROM expenses
        WHERE LOWER(category) LIKE LOWER(?) OR LOWER(note) LIKE LOWER(?) OR date LIKE ?
    '''
    like_pattern = f'%{keyword}%'
    cursor.execute(query, (like_pattern, like_pattern, like_pattern))
    results = cursor.fetchall()

    if results:
        print("\nMatching Expenses:")
        for row in results:
            try:
                readable_date = datetime.strptime(row[3], '%Y-%m-%d').strftime('%d %b %Y')
            except ValueError:
                readable_date = row[3]
            print(f"ID: {row[0]} | Amount: {row[1]} | Category: {row[2]} | Date: {readable_date} | Note: {row[4]} | Recurring: {row[5]}")
    else:
        print("No expenses found matching the keyword.")


def show_monthly_summary():
    cursor.execute("SELECT strftime('%Y-%m', date) AS month, SUM(amount) FROM expenses GROUP BY month")
    rows = cursor.fetchall()
    print("\nMonthly Expense Summary:")
    for row in rows:
        try:
            readable_month = datetime.strptime(row[0], '%Y-%m').strftime('%B %Y')
        except ValueError:
            readable_month = row[0]
        print(f"Month: {readable_month} | Total: {row[1]:.2f}")


def show_category_breakdown():
    cursor.execute("SELECT category, SUM(amount) FROM expenses GROUP BY category")
    rows = cursor.fetchall()
    print("\nCategory Breakdown:")
    for row in rows:
        print(f"Category: {row[0]} | Total: {row[1]:.2f}")

def export_to_csv(filename="expenses.csv"):
    cursor.execute("SELECT * FROM expenses")
    rows = cursor.fetchall()
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["ID", "Amount", "Category", "Date", "Note", "Recurring"])
        writer.writerows(rows)
    print(f"Exported to {filename}")

# --- MAIN MENU ---
def main():
    if getpass.getpass("Enter password: ") != MASTER_PASSWORD:
        print("Access denied.")
        return

    while True:
        print("\nExpense Manager Menu:")
        print("1. List expenses")
        print("2. Add expense")
        print("3. Update expense")
        print("4. Delete expense")
        print("5. Search by keyword")
        print("6. Show monthly summary")
        print("7. Show category breakdown")
        print("8. Export to CSV")
        print("9. Exit")

        choice = input("Enter your choice (1-9): ").strip()

        if choice == '1':
            list_expenses()
        elif choice == '2':
            try:
                amount = float(input("Enter amount: "))
                category = input("Enter category: ")
                date = input("Enter date (YYYY-MM-DD): ")
                datetime.strptime(date, "%Y-%m-%d")
                note = input("Enter note: ")
                recurring = input("Recurring? (monthly/weekly/none): ") or None
                add_expense(amount, category, date, note, recurring)
            except ValueError:
                print("Invalid input. Please check amount and date format.")
        elif choice == '3':
            try:
                expenses = list_expenses()
                if not expenses:
                    continue
                expense_id = int(input("Enter ID to update: "))
                amount = float(input("Enter new amount: "))
                category = input("Enter new category: ")
                date = input("Enter new date (YYYY-MM-DD): ")
                datetime.strptime(date, "%Y-%m-%d")
                note = input("Enter new note: ")
                recurring = input("Recurring? (monthly/weekly/none): ") or None
                update_expense(expense_id, amount, category, date, note, recurring)
            except ValueError:
                print("Invalid input.")
        elif choice == '4':
            expenses = list_expenses()
            if not expenses:
                continue
            try:
                expense_id = int(input("Enter ID to delete: "))
                delete_expense(expense_id)
            except ValueError:
                print("Invalid ID.")
        elif choice == '5':
            keyword = input("Enter keyword to search: ")
            search_expense_by_keyword(keyword)
        elif choice == '6':
            show_monthly_summary()
        elif choice == '7':
            show_category_breakdown()
        elif choice == '8':
            export_to_csv()
        elif choice == '9':
            print("Exiting application.")
            break
        else:
            print("Invalid choice. Enter a number between 1 and 9.")

    conn.close()

if __name__ == "__main__":
    main()