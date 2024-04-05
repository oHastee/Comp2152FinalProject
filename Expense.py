from datetime import datetime
import mysql.connector

from Expense_Category import ExpenseCategory

class Expense:
    def __init__(self, amount: float, category: 'ExpenseCategory', date: str):
        self.__amount = amount
        self.__category = category
        try:
            self.__date = datetime.strptime(date, '%Y-%m-%d')
        except ValueError as e:
            print(f"Error creating expense: {e}. Please enter the date in YYYY-MM-DD format.")
            raise ValueError("Invalid date format.") from e

    def get_category_id(self):
        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="REMOVED_USERNAME",
                password="[REDACTED_PASSWORD]",
                database="ExpenseTracker"
            )
            cursor = connection.cursor()

            # Fetch the CategoryID based on the category name
            cursor.execute("SELECT CategoryID FROM ExpenseCategories WHERE CategoryName = %s", (self.get_category(),))
            result = cursor.fetchone()
            if result:
                return result[0]
            else:
                print(f"Category '{self.get_category()}' does not exist in the database.")
                return None

        except mysql.connector.Error as error:
            print(f"Error fetching category ID from database: {error}")
            return None

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    def add_to_database(self):
        try:
            category_id = self.get_category_id()
            if category_id is None:
                return False

            connection = mysql.connector.connect(
                host="localhost",
                user="REMOVED_USERNAME",
                password="[REDACTED_PASSWORD]",
                database="ExpenseTracker"
            )
            cursor = connection.cursor()

            # Insert expense into the database
            cursor.execute("INSERT INTO Expenses (CategoryID, Amount, Date) VALUES (%s, %s, %s)",
                           (category_id, self.__amount, self.__date))
            connection.commit()
            print("Expense added to the database.")
            return True

        except mysql.connector.Error as error:
            print(f"Error adding expense to the database: {error}")
            return False

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    def get_amount(self) -> float:
        return self.__amount

    def get_date(self) -> datetime:
        return self.__date

    def get_category(self) -> str: # To get the string variation of category
        return self.__category.get_name()

    def get_category_object(self) -> ExpenseCategory:
        return self.__category
