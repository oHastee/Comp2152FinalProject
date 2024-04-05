# Main function
from calendar import month_name

from Expense import Expense
from Expense_Category import ExpenseCategory
from Expense_Record import ExpenseRecord
from Expense_Report import ExpenseReport
from Preset_Categories import preset_categories


def main():
    # Create an empty list to store expense reports
    report_list = []

    expense_report2023 = ExpenseReport(2023, preset_categories)
    expense_report2024 = ExpenseReport(2024, preset_categories)

    report_list.append(expense_report2023)
    report_list.append(expense_report2024)

    # Create an instance of ExpenseRecord
    expense_record = ExpenseRecord()

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

        # Retrieve the expense record for the entered month and year
        monthly_expenses = expense_record.calculate_monthly_expenses(month, year)

        # Check if there are any expenses for the entered month and year
        if monthly_expenses:
            # Display the monthly expenses for the entered month and year
            print(f"\nMonthly expenses for {month}/{year}:")
            for category, amount in monthly_expenses.items():
                # Format the amount to always display two decimal places
                formatted_amount = "{:.2f}".format(amount)
                print(f"{category}: {formatted_amount}")

            # Calculate and display the total monthly spending
            total_monthly_spending = expense_record.calculate_total_monthly_spending(month, year)
            formatted_total_spending = "{:.2f}".format(total_monthly_spending)
            print(f"\nTotal Monthly Spending: {formatted_total_spending}")
        else:
            print(f"No expenses found for {month}/{year}.")

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
