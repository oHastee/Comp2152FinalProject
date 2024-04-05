from calendar import month_name
from Expense_Record import ExpenseRecord

class ExpenseReport:
    def __init__(self, expense_record: ExpenseRecord, expense_categories: dict):
        self.expense_record = expense_record  # Reference to the ExpenseRecord instance
        self.expense_categories = expense_categories  # Dictionary of expense categories

        # Initialize expense records for each month of the year
        self.expense_records = {}
        for month in range(1, 13):
            month_name_str = month_name[month]
            self.expense_records[month_name_str] = self.expense_record

    def generate_monthly_report(self, month, year):
        # Retrieve the expense record for the entered month and year
        monthly_expenses = self.expense_records[month].calculate_monthly_expenses(month, year)

        # Check if there are any expenses for the entered month and year
        if monthly_expenses:
            # Display the monthly expenses for the entered month and year
            report = f"\nMonthly expenses for {month}/{year}:\n"
            for category, amount in monthly_expenses.items():
                # Format the amount to always display two decimal places
                formatted_amount = "{:.2f}".format(amount)
                report += f"{category}: {formatted_amount}\n"

                # Calculate the yearly average expenses for the current category
                yearly_average_expenses = self.expense_records[month].calculate_yearly_average(year)
                yearly_average = yearly_average_expenses.get(category, 0.0)

                # Compare monthly expenses with yearly average and include in the report
                comparison = "higher" if amount > yearly_average else "lower" if amount < yearly_average else "equal"
                report += f"\nYearly Average: {yearly_average:.2f}\n"
                report += f"Your expense is {comparison} than the yearly average.\n"

            # Calculate and display the total monthly spending
            total_monthly_spending = self.expense_records[month].calculate_total_monthly_spending(month, year)
            formatted_total_spending = "{:.2f}".format(total_monthly_spending)
            report += f"\nTotal Monthly Spending: {formatted_total_spending}"
            return report
        else:
            return f"No expenses found for {month}/{year}."
