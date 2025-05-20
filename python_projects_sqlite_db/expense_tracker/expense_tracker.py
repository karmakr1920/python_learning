import sqlite3
conn = sqlite3.connect('expense_tracker.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS expenses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        amount REAL NOT NULL,
        category TEXT NOT NULL,
        date TEXT NOT NULL,
        note TEXT
    )
''')

def list_expenses():
    cursor.execute("SELECT * FROM expenses")
    expenses = cursor.fetchall()
    if not expenses:
        print("No expenses found.")
        return []
    print("\nList of expenses:")
    for expense in expenses:
        print(f"ID: {expense[0]} | Amount: {expense[1]} | Category: {expense[2]} | Date: {expense[3]} | Note: {expense[4]}")
    return expenses

def add_expense(amount, category, date, note):
    cursor.execute("INSERT INTO expenses(amount, category, date, note) VALUES (?, ?, ?, ?)", (amount, category, date, note))
    conn.commit()
    print("Expense added successfully.")
 
def update_expense(expense_id, amount, category, date, note):
    cursor.execute("SELECT * FROM expenses WHERE id = ?", (expense_id,))
    if cursor.fetchone() is None:
        print("Expense ID not found.")
        return
    cursor.execute("UPDATE expenses SET amount = ?, category = ?, date = ?, note = ? WHERE id = ?", (amount, category, date, note,expense_id))
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
        SELECT id, amount, category, date, note
        FROM expenses
        WHERE category LIKE ? OR note LIKE ? OR date LIKE ?
    '''
    like_pattern = f'%{keyword}%'
    cursor.execute(query, (like_pattern, like_pattern, like_pattern))
    results = cursor.fetchall()

    if results:
        print("\nMatching Expenses:")
        print("-" * 50)
        for row in results:
            print(f"ID: {row[0]} | Amount: {row[1]} | Category: {row[2]} | Date: {row[3]} | Note: {row[4]}")
    else:
        print("\nNo expenses found matching the keyword.")
def main():
    while True:
        print("\nExpense Manager Menu:")
        print("1. List expenses")
        print("2. Add expense")
        print("3. Update expense")
        print("4. Delete expense")
        print("5. Search expense by any keyword")
        print("6. Exit")
        choice = input("Enter your choice (1-9): ").strip()

        if choice == '1':
            list_expenses()
        elif choice == '2':
            amount = input("Enter expense amount: ")
            category = input("Enter expense category: ")
            date = input("Enter expense date: ")
            note = input("Enter expense note: ")
            add_expense(amount, category, date, note)
        elif choice == '3':
            expenses = list_expenses()
            if not expenses:
                continue
            expense_id = input("Enter expense ID to update: ")
            amount = input("Enter expense amount: ")
            category = input("Enter expense category: ")
            date = input("Enter expense date: ")
            note = input("Enter expense note: ")
            update_expense(expense_id, amount, category, date, note)
        elif choice == '4':
            expenses = list_expenses()
            if not expenses:
                continue
            expense_id = input("Enter expense ID to delete: ")
            delete_expense(expense_id)
        elif choice == '5':
            keyword = input("Enter a keyword to search: ")
            search_expense_by_keyword(keyword)
            pass
        elif choice == '6':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 9.")

    conn.close()

if __name__ == "__main__":
    main()