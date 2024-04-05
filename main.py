
from Expense import Expense
from Expense_Category import ExpenseCategory
from Expense_Record import ExpenseRecord
from Expense_Report import ExpenseReport
from Preset_Categories import preset_categories


def main():
    # Create an instance of ExpenseRecord
    expense_record = ExpenseRecord()

    # Create an instance of ExpenseReport and pass the expense_record instance to it
    expense_report = ExpenseReport(expense_record, preset_categories)

    def display_menu():
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Monthly Expense Report")
        print("3. View Yearly Expense Report")
        print("4. Exit")

    def add_expense():
        category_name = input("Enter the expense category: ")  # Assuming category is already defined
        amount = float(input("Enter the expense amount: "))
        date = input("Enter the expense date (YYYY-MM-DD): ")
        expense = Expense(amount, ExpenseCategory(category_name), date)
        expense_record.add_expense(expense)  # Call add_expense on expense_record instance

    def view_monthly_expenses():
        year = int(input("Enter the year: "))
        month = input("Enter the month (e.g., January, February, etc.): ")
        print(expense_report.generate_monthly_report(month,year))

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_monthly_expenses()
        # elif choice == '3':
            #
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
