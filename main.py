from expense import add_expense
from report import total_spending, category_summary

while True:
    print("\nExpense Tracker")
    print("1. Add Expense")
    print("2. Total Spending")
    print("3. Category Summary")
    print("4. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        total_spending()

    elif choice == "3":
        category_summary()

    elif choice == "4":
        break

    else:
        print("Invalid option")
