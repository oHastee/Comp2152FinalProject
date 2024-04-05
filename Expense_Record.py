from Expense import Expense
from collections import defaultdict


class ExpenseRecord:
    def __init__(self):
        self.__expenses = []

    def get_expenses(self):
        return self.__expenses

    def add_expense(self, expense: Expense):
        self.__expenses.append(expense)

    def calculate_monthly_expenses(self, month: str, year: int) -> dict:
        total_expenses_per_category = defaultdict(float)
        month_lower = month.lower()  # Convert month parameter to lowercase

        # Iterate through expenses and accumulate expenses for each category
        for expense in self.__expenses:
            if expense.get_date().strftime('%B').lower() == month_lower and expense.get_date().year == year:
                category_name = expense.get_category()  # .get_name() Commented out to work
                total_expenses_per_category[category_name] += expense.get_amount()

        return total_expenses_per_category

    def calculate_total_monthly_spending(self, month: str, year: int) -> float:
        total_spending = 0.0
        month_lower = month.lower()  # Convert month parameter to lowercase

        # Iterate through expenses and accumulate total spending for the specified month and year
        for expense in self.__expenses:
            if (expense.get_date().strftime('%B').lower() == month_lower and
                    expense.get_date().year == year):
                total_spending += expense.get_amount()

        return round(total_spending, 2)

    def calculate_yearly_average(self, year: int) -> dict:
        # Dictionary to store total expenses and count of expenses for each category
        category_totals = defaultdict(lambda: {'total': 0.0, 'count': 0})

        # Iterate through all expenses for the specified year
        for expense in self.__expenses:
            if expense.get_date().year == year:
                category_name = expense.get_category()  # .get_name() Commented out to work
                category_totals[category_name]['total'] += expense.get_amount()
                category_totals[category_name]['count'] += 1

        # Dictionary to store yearly average expenses for each category
        yearly_average = {}

        # Calculate yearly average expenses for each category
        for category_name, data in category_totals.items():
            total_expenses = data['total']
            expense_count = data['count']
            if expense_count == 0:
                yearly_average[category_name] = 0.0  # Handle division by zero
            else:
                yearly_average[category_name] = round(total_expenses / expense_count,
                                                      2)  # Round off to 2 decimal places

        return yearly_average
