from storage import load_expenses, save_expenses
from datetime import date

def add_expense():
    amount = float(input("Enter amount: "))
    category = input("Enter category (food/travel/bills): ")

    expense = {
        "amount": amount,
        "category": category,
        "date": str(date.today())
    }

    expenses = load_expenses()
    expenses.append(expense)
    save_expenses(expenses)

    print("Expense added successfully!")
