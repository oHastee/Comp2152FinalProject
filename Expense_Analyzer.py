from Expense_Record import ExpenseRecord
from Expense_Report import ExpenseReport
import datetime

class ExpenseAnalyzer:
    def __init__(self):
        pass

    @staticmethod
    def print_total_expenses_by_category_str(expense_report: ExpenseReport, month: int):
        total_expenses = expense_report.calculate_total_expenses_for_month(month)

        if isinstance(total_expenses, float):
            print(f"Total monthly expense: ${total_expenses:.2f}")
        else:
            for category, total_expense in total_expenses["total_expenses_per_category"].items():
                print(f"{category}: ${total_expense:.2f}")

    @staticmethod
    def print_total_expenses_by_category_obj(expense_report: ExpenseReport, month: int):
        total_expenses = expense_report.calculate_total_expenses_for_month(month)

        if isinstance(total_expenses, float):
            return {"Total monthly expense": total_expenses}
        else:
            return total_expenses["total_expenses_per_category"]

    @staticmethod
    def calculate_monthly_expenses(expense_record: ExpenseRecord, month: str):
        return expense_record.calculate_monthly_expenses(month)

    @staticmethod
    def calculate_yearly_average_expenses(expense_record: ExpenseRecord):
        return expense_record.calculate_yearly_average()

    @staticmethod
    def add_expenses_from_record(expense_report: ExpenseReport, expense_record: ExpenseRecord):
        for expense in expense_record.get_expenses():
            expense_report.add_expense(expense)

    @staticmethod
    def compare_monthly_expenses_with_annual_average(expense_record, yearly_average_expenses):
        # Calculate monthly expenses for each category
        monthly_expenses = {}
        for month in range(1, 13):
            monthly_expenses[month] = expense_record.calculate_monthly_expenses(month)

        # Print comparison
        print("Comparison of Monthly Expenses with Annual Average:")
        for month, expenses in monthly_expenses.items():
            print(f"\nMonth: {datetime.date(1900, month, 1).strftime('%B')}")
            for category, expense in expenses.items():
                annual_average = yearly_average_expenses[category]
                print(f"{category}: Monthly: ${expense:.2f}, Annual Average: ${annual_average:.2f}")
