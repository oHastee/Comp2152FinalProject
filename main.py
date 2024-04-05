from calendar import month_name
from datetime import datetime
import MySQLdb


from Expense import Expense
from Expense_Category import ExpenseCategory
from Expense_Record import ExpenseRecord
from Expense_Report import ExpenseReport
from Preset_Categories import preset_categories

def main():
    # Replace placeholders with your actual database details
    connection = MySQLdb.connect(
        host="localhost",
        user="REMOVED_USERNAME",
        password="[REDACTED_PASSWORD]",
        database="ExpenseTracker"
    )

    cursor = connection.cursor()

    # Create an instance of ExpenseRecord
    expense_record = ExpenseRecord()

    # Create an instance of ExpenseReport and pass the expense_record instance to it
    expense_report = ExpenseReport(expense_record, preset_categories)

    def display_menu():
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Monthly Expense Report")
        print("3. Exit")

    def add_expense():
        while True:
            category_name = input("Enter the expense category: ")
            if not category_name.replace(' ', '').isalpha():
                print("Error: Category name must be a alphanumeric character.")
                continue

            # Check if the category already exists in the database, if not, add it
            try:
                category = ExpenseCategory(category_name)
                category.add_to_database()
            except Exception as e:
                print(f"Error adding category to database: {e}")

            while True:
                try:
                    amount = float(input("Enter the expense amount: "))
                    break
                except ValueError:
                    print("Error: Invalid amount. Please enter a valid number.")

            while True:
                date = input("Enter the expense date (YYYY-MM-DD): ")
                try:
                    datetime.strptime(date, '%Y-%m-%d')
                    break
                except ValueError:
                    print("Error: Invalid date format. Please enter the date in YYYY-MM-DD format.")

            try:
                expense = Expense(amount, ExpenseCategory(category_name), date)
                expense.add_to_database()
            except ValueError as e:
                print(f"Error creating expense: {e}")
                continue


            while True:
                add_another = input("Do you want to add another expense? (yes/no): ").lower()
                if add_another == 'yes':
                    break
                elif add_another == 'no':
                    return
                else:
                    print("Error: Invalid input. Please enter 'yes' or 'no'.")

    def view_monthly_expenses():
        while True:
            try:
                year = int(input("Enter the year: "))
                break
            except ValueError:
                print("Error: Invalid year. Please enter a valid year.")

        while True:
            month = input("Enter the month (e.g., January, February, etc.): ")
            month = month.capitalize()  # Convert the first letter to uppercase
            if month in month_name:
                break
            else:
                print("Error: Invalid month. Please enter a valid month.")

        try:
            print(expense_report.generate_monthly_report(month, year))
        except Exception as e:
            print(f"Error generating report: {e}")

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_monthly_expenses()
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

    cursor.close()
    connection.close()


if __name__ == "__main__":
    main()
