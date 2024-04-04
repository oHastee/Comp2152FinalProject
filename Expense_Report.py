from calendar import month_name
from collections import defaultdict
from Expense_Record import ExpenseRecord

class ExpenseReport:
    def __init__(self, year: int, expense_categories: dict):
        self.__year = year
        self.expense__records = {}  # Dictionary to store expense records for each month
        self.expense__categories = expense_categories  # Dictionary of expense categories

        # Initialize expense records for each month of the year
        for month in range(1, 13):
            month_name_str = month_name[month]
            self.expense__records[month_name_str] = ExpenseRecord()

    def get_year(self) -> int:
        return self.__year

    def generate_monthly_report(self, month):
        monthly_expense_record = self.expense__records[month]
        total_monthly_expense = 0.0
        total_expenses_per_category = defaultdict(float)

        # Retrieve expenses for the specified month
        expenses = monthly_expense_record.get_expenses()

        # Accumulate expenses for each category and total monthly expense
        for expense in expenses:
            category_name = expense.get_category()  # .get_name() Commented out to work
            total_expenses_per_category[category_name] += expense.get_amount()
            total_monthly_expense += expense.get_amount()

        report = f"Monthly Report for {month}/{self.__year}:\n"
        report += f"Total Monthly Expense: {total_monthly_expense}\n"
        report += "Total Expenses by Category:\n"
        for category, amount in total_expenses_per_category.items():
            report += f"{category}: {amount}\n"

        return report

    def generate_yearly_report(self):
        yearly_average = {}
        category_totals = defaultdict(lambda: {'total': 0.0, 'count': 0})

        # Aggregate total expenses and count of expenses for each category across all months
        for month, record in self.expense__records.items():
            for category, data in record.calculate_monthly_expenses(month).items():
                category_totals[category]['total'] += data
                category_totals[category]['count'] += 1

        # Calculate yearly average expenses for each category
        yearly_report = f"Yearly Report for {self.__year}:\n"
        yearly_report += "Average Expenses for Each Category:\n"
        for category, data in category_totals.items():
            total_expenses = data['total']
            expense_count = data['count']
            yearly_average[category] = round(total_expenses / expense_count, 2) if expense_count > 0 else 0.0
            yearly_report += f"{category}: {yearly_average[category]}\n"

        return yearly_report

    def compare_monthly_with_yearly(self, month):
        monthly_expense = self.expense__records[month].calculate_monthly_expenses(month)
        yearly_average = self.calculate_yearly_average()
        comparison = "higher" if monthly_expense > yearly_average else "lower" if monthly_expense < yearly_average else "equal"

        comparison_report = f"Comparison of Monthly Expenses for {month}/{self.__year} with Yearly Average:\n"
        comparison_report += f"Monthly expense is {comparison} than the yearly average."

        return comparison_report

    def calculate_percentage(self, month):
        total_monthly_expense = self.expense__records[month].calculate_monthly_expenses(month)
        total_expenses = self.expense__records[month].calculate_monthly_expenses(month)

        percentage_report = f"Percentage of Expenses from Each Category for {month}/{self.__year}:\n"
        for category, amount in total_expenses.items():
            percentage = (amount / total_monthly_expense) * 100
            percentage_report += f"{category}: {percentage:.2f}%\n"

        return percentage_report

    def calculate_yearly_average(self):
        total_expenses = sum(record.calculate_monthly_expenses(month) for month, record in self.expense__records.items())
        total_months = sum(1 for _ in self.expense__records)
        return total_expenses / total_months
