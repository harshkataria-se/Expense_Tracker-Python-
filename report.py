from storage import load_expenses

def total_spending():
    expenses = load_expenses()
    total = sum(e["amount"] for e in expenses)
    print("Total spending:", total)

def category_summary():
    expenses = load_expenses()
    summary = {}

    for e in expenses:
        cat = e["category"]
        summary[cat] = summary.get(cat, 0) + e["amount"]

    print("Category Summary:")
    for k, v in summary.items():
        print(k, ":", v)
