import csv
import os
from datetime import datetime

# ---------------- CONFIG ----------------
BASE_DIR = os.path.dirname(__file__)
# DATA_FOLDER = os.path.join(BASE_DIR, "Expense_Tracker")
FILE_NAME = os.path.join(BASE_DIR, "expenses.csv")
# --------------------------------------


# ----------- FILE INITIALIZATION --------
def init_file():
    try:
        os.makedirs(BASE_DIR, exist_ok=True)

        if not os.path.exists(FILE_NAME):
            with open(FILE_NAME, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(["Date", "Category", "Amount", "Description"])

    except PermissionError:
        print("\nPermission denied. Cannot create data folder/file.")
        exit()
    except Exception as e:
        print("\nUnexpected error:", e)
        exit()


# ----------- SAFE INPUT FUNCTIONS -------
def safe_string_input(message):
    while True:
        value = input(message).strip()
        if value == "":
            print("\nInput cannot be empty")
        else:
            return value


def safe_float_input(message):
    while True:
        try:
            value = float(input(message))
            if value <= 0:
                print("\nValue must be positive")
            else:
                return value
        except ValueError:
            print("\nPlease enter a valid number")


# -------------- ADD EXPENSE -------------
def add_expense():
    print("\nAdd New Expense")

    date = datetime.now().strftime("%Y-%m-%d")
    category = safe_string_input("Category: ")
    amount = safe_float_input("Amount: ")
    description = input("Description (optional): ").strip()

    try:
        with open(FILE_NAME, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([date, category, amount, description])
        print("\nExpense added successfully!")

    except PermissionError:
        print("\nPermission denied while writing file")
    except Exception as e:
        print("\nUnexpected error:", e)


# -------------- VIEW EXPENSES ------------
def view_expenses():
    try:
        with open(FILE_NAME, 'r') as f:
            reader = csv.reader(f)
            rows = list(reader)

            if len(rows) <= 1:
                print("\nNo expenses recorded yet")
                return

            print("\nDate         Category        Amount     Description")
            print("-" * 60)

            total = 0
            for row in rows[1:]:
                try:
                    print(f"{row[0]:<12} {row[1]:<15} {float(row[2]):<10.2f} {row[3]}")
                    total += float(row[2])
                except (IndexError, ValueError):
                    print("⚠️ Skipping corrupted row:", row)

            print("-" * 60)
            print(f"💰 Total Expenses: {total:.2f}")

    except FileNotFoundError:
        print("\nExpense file not found")
    except Exception as e:
        print("\nUnexpected error:", e)


# -------------- SEARCH CATEGORY ----------
def search_by_category():
    category = safe_string_input("\nEnter category to search: ").lower()

    try:
        with open(FILE_NAME, 'r') as f:
            reader = csv.reader(f)
            found = False
            total = 0

            print("\nDate         Category        Amount     Description")
            print("-" * 60)

            for row in reader:
                if len(row) >= 3 and row[1].lower() == category:
                    print(f"{row[0]:<12} {row[1]:<15} {float(row[2]):<10.2f} {row[3]}")
                    total += float(row[2])
                    found = True

            if not found:
                print("❌ No records found")
            else:
                print("-" * 60)
                print(f"Total for {category}: {total:.2f}")

    except FileNotFoundError:
        print("\nExpense file not found")
    except Exception as e:
        print("\nUnexpected error:", e)


# -------------- DELETE ALL ---------------
def delete_all():
    confirm = input("⚠️ Are you sure you want to delete ALL expenses? (yes/no): ").lower()

    if confirm == "yes":
        try:
            with open(FILE_NAME, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(["Date", "Category", "Amount", "Description"])
            print("\nAll records deleted")
        except Exception as e:
            print("\nError:", e)
    else:
        print("\nDeletion cancelled")


# -------------- DELETE BY CATEGORY -------
def delete_by_category():
    category = safe_string_input("\nEnter category to delete: ").lower()

    try:
        with open(FILE_NAME, 'r') as f:
            reader = csv.reader(f)
            rows = list(reader)

        if len(rows) <= 1:
            print("\nNo expenses recorded yet")
            return

        header = rows[0]
        data = rows[1:]

        new_data = []
        deleted_count = 0

        for row in data:
            if row[1].lower() == category:
                deleted_count += 1
            else:
                new_data.append(row)

        if deleted_count == 0:
            print(f"\nNo records found for category '{category}'")
            return

        confirm = input(
            f"\nAre you sure you want to delete {deleted_count} record(s) of '{category}'? (yes/no): "
        ).lower()

        if confirm != "yes":
            print("\nDeletion cancelled")
            return

        with open(FILE_NAME, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(header)
            writer.writerows(new_data)

        print(f"\n✅ {deleted_count} record(s) deleted successfully")

    except Exception as e:
        print("\nUnexpected error:", e)


# ---------------- MENU -------------------
def menu():
    while True:
        print("\n" + "=" * 40)
        print("💰 EXPENSE TRACKER")
        print("=" * 40)
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Search by Category")
        print("4. Delete Expenses by Category")
        print("5. Delete All Expenses") 
        print("6. Exit")

        choice = input("Choose option (1-6): ").strip()

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            search_by_category()
        elif choice == '4':
            delete_by_category()
        elif choice == '5':
            delete_all()
        elif choice == '6':
            print("\nGoodbye! Happy Saving!")
            break
        else:
            print("\nInvalid choice. Enter 1-6 only")


# ------------- PROGRAM START -------------
if __name__ == "__main__":
    init_file()
    menu()
