import sqlite3
import pandas as pd
from datetime import datetime

def add_expense(date, category, description, amount):
    conn = sqlite3.connect('expenses.db')
    c = conn.cursor()
    c.execute('''
    INSERT INTO expenses (date, category, description, amount) VALUES (?, ?, ?, ?)
    ''', (date, category, description, amount))
    conn.commit()
    conn.close()

def view_expenses():
    conn = sqlite3.connect('expenses.db')
    c = conn.cursor()
    c.execute('SELECT * FROM expenses')
    rows = c.fetchall()
    conn.close()
    return rows

def delete_expense(expense_id):
    conn = sqlite3.connect('expenses.db')
    c = conn.cursor()
    c.execute('DELETE FROM expenses WHERE id=?', (expense_id,))
    conn.commit()
    conn.close()

def generate_report():
    conn = sqlite3.connect('expenses.db')
    df = pd.read_sql_query('SELECT * FROM expenses', conn)
    report = df.groupby(['category'])['amount'].sum().reset_index()
    conn.close()
    return report

if __name__ == '__main__':
    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Delete Expense")
        print("4. Generate Report")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            date = input("Enter date (YYYY-MM-DD): ")
            category = input("Enter category: ")
            description = input("Enter description: ")
            amount = float(input("Enter amount: "))
            add_expense(date, category, description, amount)
            print("Expense added successfully!")
        elif choice == '2':
            expenses = view_expenses()
            for expense in expenses:
                print(expense)
        elif choice == '3':
            expense_id = int(input("Enter expense ID to delete: "))
            delete_expense(expense_id)
            print("Expense deleted successfully!")
        elif choice == '4':
            report = generate_report()
            print(report)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")
