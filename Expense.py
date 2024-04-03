from datetime import datetime
from Expense_Category import ExpenseCategory


class Expense:
    def __init__(self, amount: float, category: 'ExpenseCategory', date: str):
        self.__amount = amount
        self.__category = category
        self.__date = datetime.strptime(date, '%Y-%m-%d')  # Convert date string to datetime object
        # #datetime.now() Wanted to use datetime.now as its more realistic
        # But dosent really work for testing purposes

    def get_amount(self) -> float:
        return self.__amount

    def get_date(self) -> datetime:
        return self.__date

    def get_category(self) -> str: # To get the str varation of category
        return self.__category.get_name()

    def get_category_object(self) -> ExpenseCategory:
        return self.__category

