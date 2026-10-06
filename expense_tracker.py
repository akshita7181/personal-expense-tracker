```python
import csv
import os
from datetime import datetime

FILE_NAME = "expenses.csv"


# Create the CSV file if it does not exist
def create_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Amount", "Description"])


# Add a new expense
def add_expense():
    print("\n--- Add Expense ---")

    category = input("Enter category (Food/Travel/Shopping/Other): ")

    try:
        amount = float(input("Enter amount: ₹"))
    except ValueError:
        print("Please enter a valid amount.")
        return

    description = input("Enter description: ")
    date = datetime.now().strftime("%Y-%m-%d")

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount, description])

    print("Expense added successfully!")


# Display all expenses
def view_expenses():
    print("\n--- All Expenses ---")

    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)

        expenses_found = False

        for row in reader:
            expenses_found = True
            print(
                f"{row['Date']} | "
                f"{row['Category']} | "
                f"₹{row['Amount']} | "
                f"{row['Description']}"
            )

        if not expenses_found:
            print("No expenses recorded yet.")


# Calculate total spending
def total_spending():
    total = 0

    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            total += float(row["Amount"])

    print(f"\nTotal spending: ₹{total:.2f}")


# Show spending category-wise
def category_summary():
    categories = {}

    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            category = row["Category"]
            amount = float(row["Amount"])

            if category in categories:
                categories[category] += amount
            else:
                categories[category] = amount

    print("\n--- Category-wise Spending ---")

    if not categories:
        print("No expenses recorded yet.")
        return

    for category, amount in categories.items():
        print(f"{category}: ₹{amount:.2f}")


# Find the largest expense
def highest_expense():
    highest = None

    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            amount = float(row["Amount"])

            if highest is None or amount > float(highest["Amount"]):
                highest = row

    print("\n--- Highest Expense ---")

    if highest:
        print(f"Date: {highest['Date']}")
        print(f"Category: {highest['Category']}")
        print(f"Amount: ₹{highest['Amount']}")
        print(f"Description: {highest['Description']}")
    else:
        print("No expenses recorded yet.")


# Main menu
def main():
    create_file()

    while True:
        print("\n==============================")
        print("     PERSONAL EXPENSE TRACKER")
        print("==============================")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Spending")
        print("4. Category-wise Spending")
        print("5. Highest Expense")
        print("6. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            total_spending()

        elif choice == "4":
            category_summary()

        elif choice == "5":
            highest_expense()

        elif choice == "6":
            print("Thank you for using the Expense Tracker!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
```