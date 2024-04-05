from calendar import month_name
import MySQLdb
from collections import defaultdict
from Expense_Record import ExpenseRecord

class ExpenseReport:
    def __init__(self, expense_record: ExpenseRecord, expense_categories: dict):
        self.expense_record = expense_record  # Reference to the ExpenseRecord instance
        self.expense_categories = expense_categories  # Dictionary of expense categories

    def generate_monthly_report(self, month, year):
        try:
            # Replace placeholders with your actual database details
            connection = MySQLdb.connect(
                host="localhost",
                user="root",
                password="Backugan1!",
                database="ExpenseTracker"
            )

            cursor = connection.cursor()

            # Retrieve expenses for the entered month and year from the database
            cursor.execute("""
                SELECT c.CategoryName, SUM(e.Amount) 
                FROM Expenses e
                INNER JOIN ExpenseCategories c ON e.CategoryID = c.CategoryID
                WHERE YEAR(e.Date) = %s AND MONTH(e.Date) = %s
                GROUP BY c.CategoryName
            """, (year, list(month_name).index(month)))

            monthly_expenses = {category: amount for category, amount in cursor.fetchall()}

            # Calculate yearly average expenses for each category
            cursor.execute("""
                SELECT c.CategoryName, AVG(e.Amount)
                FROM Expenses e
                INNER JOIN ExpenseCategories c ON e.CategoryID = c.CategoryID
                WHERE YEAR(e.Date) = %s
                GROUP BY c.CategoryName
            """, (year,))
            yearly_average_expenses = {category: avg_amount for category, avg_amount in cursor.fetchall()}

            cursor.close()
            connection.close()

            # Check if there are any expenses for the entered month and year
            if monthly_expenses:
                total_monthly_spending = sum(monthly_expenses.values())  # Calculate the total monthly spending

                # Display the monthly expenses for the entered month and year
                report = f"\nMonthly expenses for {month}/{year}:\n"
                for category, amount in monthly_expenses.items():
                    # Format the amount to always display two decimal places
                    formatted_amount = "{:.2f}".format(amount)
                    report += f"\n{category}: {formatted_amount}\n"

                    # Compare monthly expenses with yearly average and include in the report
                    yearly_average = yearly_average_expenses.get(category, 0.0)
                    comparison = "higher" if amount > yearly_average else "lower" if amount < yearly_average else "equal"
                    report += f"Yearly Average: {yearly_average:.2f}\n"
                    report += f"Your expense is {comparison} than the yearly average.\n"

                    # Calculate the percentage of expenses from the current category out of the total monthly expenses
                    try:
                        category_percentage = (amount / total_monthly_spending) * 100
                    except ZeroDivisionError:
                        category_percentage = 0.0
                    report += f"Percentage of {category} expenses: {category_percentage:.2f}%\n"

                # Format the total monthly spending to always display two decimal places
                formatted_total_spending = "{:.2f}".format(total_monthly_spending)
                report += f"\nTotal Monthly Spending: {formatted_total_spending}\n"
            else:
                report = f"No expenses found for {month}/{year}."

            return report

        except Exception as e:
            return f"Error generating report: {e}"
