from datetime import datetime
from Expense import Expense
from Expense_Record import ExpenseRecord
from Expense_Category import ExpenseCategory
from Expense_Report import ExpenseReport
from Preset_Categories import preset_categories

# Create an instance of ExpenseReport for the year 2023 with preset categories
expense_report2023 = ExpenseReport(2023, preset_categories)
expense_report2024 = ExpenseReport(2024, preset_categories)

# Create some expenses with preset categories
expense_record = ExpenseRecord()
expense_record.add_expense(Expense(100, preset_categories["Rent"], "2023-01-05"))
expense_record.add_expense(Expense(50, preset_categories["Dining Out"], "2023-01-10"))
expense_record.add_expense(Expense(80, preset_categories["Clothing"], "2023-01-15"))
expense_record.add_expense(Expense(500, preset_categories["Investments"], "2023-02-20"))

# Adding more expenses to the expense record
expense_record.add_expense(Expense(30, preset_categories["Clothing"], "2023-01-01"))
expense_record.add_expense(Expense(50, preset_categories["Clothing"], "2023-03-15"))
expense_record.add_expense(Expense(60, preset_categories["Clothing"], "2023-04-20"))

expense_record.add_expense(Expense(70, preset_categories["Dining Out"], "2023-01-05"))
expense_record.add_expense(Expense(80, preset_categories["Dining Out"], "2023-06-10"))
expense_record.add_expense(Expense(90, preset_categories["Dining Out"], "2023-07-15"))

expense_record.add_expense(Expense(1000, preset_categories["Investments"], "2023-01-01"))
expense_record.add_expense(Expense(2000, preset_categories["Investments"], "2023-09-05"))
expense_record.add_expense(Expense(1500, preset_categories["Investments"], "2023-10-10"))

# Add some custom expenses
expense_record.add_expense(Expense(24.99, ExpenseCategory("Rent"), "2023-03-29"))
expense_record.add_expense(Expense(50, ExpenseCategory("Rent"), "2024-01-02"))

expense_report2024.expense__records["January"].add_expense(Expense(100, preset_categories["Rent"], "2024-01-05"))
expense_report2024.expense__records["January"].add_expense(Expense(50, preset_categories["Dining Out"], "2024-01-10"))
expense_report2024.expense__records["January"].add_expense(Expense(80, preset_categories["Clothing"], "2024-01-15"))
expense_report2024.expense__records["February"].add_expense(Expense(500, preset_categories["Investments"], "2024-02-20"))

# Print reports
monthly_report = expense_report2024.generate_monthly_report("January")
print(monthly_report)

print(expense_report2023.generate_yearly_report())

