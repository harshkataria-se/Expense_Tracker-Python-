import json

FILE = "data.json"

def load_expenses():
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except:
        return []

def save_expenses(expenses):
    with open(FILE, "w") as f:
        json.dump(expenses, f, indent=4)