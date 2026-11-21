import json
import os

FILE_NAME = "expenses.json"


def load_expenses():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as f:
        return json.load(f)


def save_expenses(expenses):
    with open(FILE_NAME, "w") as f:
        json.dump(expenses, f, indent=4)


def add_expense():
    title = input("Expense name: ")
    try:
        amount = float(input("Amount: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    expenses = load_expenses()
    expenses.append({"title": title, "amount": amount})
    save_expenses(expenses)
    print("Expense added!")


def view_expenses():
    expenses = load_expenses()
    if not expenses:
        print("No expenses yet.")
        return

    print("\n--- Your Expenses ---")
    for i, e in enumerate(expenses, start=1):
        print(f"{i}. {e['title']} - {e['amount']}")


def show_total():
    expenses = load_expenses()
    total = sum(e["amount"] for e in expenses)
    print(f"\nTotal spent: {total}")


def delete_expense():
    expenses = load_expenses()
    if not expenses:
        print("Nothing to delete.")
        return

    view_expenses()
    try:
        number = int(input("Enter number to delete: "))
        removed = expenses.pop(number - 1)
    except (ValueError, IndexError):
        print("Invalid number.")
        return

    save_expenses(expenses)
    print(f"Deleted: {removed['title']}")


def main():
    while True:
        print("\n===== Expense Tracker =====")
        print("1. Add expense")
        print("2. View expenses")
        print("3. Show total")
        print("4. Delete expense")
        print("5. Exit")

        choice = input("Choose (1-5): ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            show_total()
        elif choice == "4":
            delete_expense()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


main()