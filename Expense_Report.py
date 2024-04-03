from Expense_Record import ExpenseRecord
from Expense_Category import ExpenseCategory

class ExpenseReport:
    def __init__(self, year: int, expense_categories: dict):
        self.year = year
        self.expense_records = {}  # Dictionary to store expense records for each month
        self.expense_categories = expense_categories  # Dictionary of expense categories

        # Initialize expense records for each month of the year
        for month in range(1, 13):
            self.expense_records[month] = ExpenseRecord()

    def add_expense(self, expense):
        # Get the month of the expense
        month = expense.get_date().month

        # Add the expense to the corresponding expense record for that month
        self.expense_records[month].add_expense(expense)

    def get_year(self):
        return self.year

    def get_monthly_expense_record(self, month):
        return self.expense_records[month]

    def calculate_total_expenses_for_month(self, month: int) -> dict:
        total_expenses_per_category = {}
        total_monthly_expense = 0.0

        # Iterate through each category and calculate total expenses for the specified month
        for category_name, category in self.expense_categories.items():
            total_expenses = 0.0
            # Get the expense record for the specified month
            monthly_expense_record = self.expense_records[month]

            # Calculate total expenses for the category in the specified month
            for expense in monthly_expense_record.get_expenses():
                if expense.get_category() == category_name:  # Compare category name directly
                    total_expenses += expense.get_amount()

            total_expenses_per_category[category_name] = total_expenses
            total_monthly_expense += total_expenses

        return {"total_expenses_per_category": total_expenses_per_category,
                "total_monthly_expense": total_monthly_expense}


