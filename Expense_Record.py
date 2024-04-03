from Expense import Expense
from collections import defaultdict


class ExpenseRecord:
    def __init__(self):
        self.__expenses = []

    def add_expense(self, expense: Expense):
        self.__expenses.append(expense)
        return self

    def get_expenses(self):
        return self.__expenses

    def calculate_monthly_expenses(self, month: str) -> float:
        total_expenses = 0.0
        month_lower = month.lower()  # Convert month parameter to lowercase

        # Check if the month matches before iterating through expenses
        expenses_in_month = [expense for expense in self.__expenses
                             if expense.get_date().strftime('%B').lower() == month_lower]

        # Iterate through expenses that match the specified month
        for expense in expenses_in_month:
            total_expenses += expense.get_amount()

        return total_expenses

    def calculate_yearly_average(self) -> dict:
        # Dictionary to store total expenses and count of expenses for each category
        category_totals = defaultdict(lambda: {'total': 0.0, 'count': 0})

        # Iterate through all expenses
        for expense in self.__expenses:
            category_name = expense.get_category()#.get_name() Commented out to work
            category_totals[category_name]['total'] += expense.get_amount()
            category_totals[category_name]['count'] += 1

        # Dictionary to store yearly average expenses for each category
        yearly_average = {}

        # Calculate yearly average expenses for each category
        for category_name, data in category_totals.items():
            total_expenses = data['total']
            expense_count = data['count']
            yearly_average[category_name] = total_expenses / expense_count

        return yearly_average
        