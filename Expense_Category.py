import mysql.connector

class ExpenseCategory:
    def __init__(self, name: str):
        if not isinstance(name, str):
            raise TypeError("Category name must be a string.")
        if not name.strip():
            raise ValueError("Category name cannot be empty.")
        self.__name = name

    def add_to_database(self):
        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="REMOVED_USERNAME",
                password="[REDACTED_PASSWORD]",
                database="ExpenseTracker"
            )
            cursor = connection.cursor()

            # Check if the category already exists in the database
            cursor.execute("SELECT * FROM ExpenseCategories WHERE CategoryName = %s", (self.__name,))
            existing_category = cursor.fetchone()
            if existing_category:
                print(f"Category '{self.__name}' already exists in the database.")
                return False

            # If the category doesn't exist, add it to the database
            cursor.execute("INSERT INTO ExpenseCategories (CategoryName) VALUES (%s)", (self.__name,))
            connection.commit()
            print(f"Category '{self.__name}' added to the database.")
            return True

        except mysql.connector.Error as error:
            print(f"Error adding category to the database: {error}")

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    def get_name(self) -> str:
        return self.__name
