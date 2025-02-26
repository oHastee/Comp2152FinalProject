# 💰 Expense Tracker Application

## 📌 Overview
The Expense Tracker Application is a user-friendly financial management tool designed to help users efficiently record, categorize, and analyze their expenses. Built with Python 🐍 and MySQL 🗃️, this application supports detailed expense reporting and budgeting by allowing users to track spending habits, identify financial patterns, and maintain better control of their personal finances.

## ✨ Features
- **Expense Entry 📝:** Easily add and categorize expenses by specifying the amount, category, and date.
- **Preset Categories 📂:** Includes predefined expense categories such as Rent, Groceries, Utilities, Transportation, Health, and more, ensuring easy organization.
- **Database Integration 🔐:** Securely stores expense data and categories in a MySQL database.
- **Detailed Reports 📊:** Generate comprehensive monthly reports, comparing monthly expenditures with yearly averages.
- **Analysis Tools 📈:** Visualize spending distribution by percentage for each expense category.
- **Error Handling ⚠️:** Robust validation and error handling for user inputs to prevent incorrect or invalid data entries.

## 🛠️ Technical Stack
- **Python 🐍**: Primary programming language used for application logic.
- **MySQL 🗃️**: Database for reliable and secure data storage.
- **MySQL Connector/Python 🔗**: Facilitates seamless interaction between Python and the MySQL database.

## 📁 Project Structure
The application follows a modular and object-oriented design, comprising the following key components:
- `Expense` 💳: Represents individual expenses, capturing amount, category, and date.
- `ExpenseCategory` 🗂️: Manages categories for classifying expenses.
- `ExpenseRecord` 📚: Handles collections of expenses and performs calculations like monthly totals and yearly averages.
- `ExpenseReport` 📃: Generates and formats monthly expense reports based on data from `ExpenseRecord`.
- `PresetCategories` 📦: Predefined categories readily available to users upon application setup.

## 🚀 Installation
1. Clone the repository:
```bash
git clone <repository-url>
```

2. Install dependencies:
```bash
pip install mysql-connector-python
```

3. Set up your MySQL database:
- Create a database named `ExpenseTracker`.
- Import necessary tables as per the provided schema.

4. Configure Database Credentials:
- Replace placeholders (`REMOVED_USERNAME`, `[REDACTED_PASSWORD]`) in the code with your actual database credentials.

## ▶️ Running the Application
Execute the main Python script:
```bash
python main.py
```

Follow the interactive prompts to manage your expenses and generate reports.

## 🔮 Future Improvements
- Integration with visualization libraries (e.g., Matplotlib or Seaborn) 📉 for graphical expense analysis.
- Mobile 📱 or web 🌐 application development for enhanced accessibility.
- Enhanced security measures 🛡️ for protecting user data.

## 📬 Contact
For further information or questions, please contact:
- **Name:** Oscar Piedrasanta Diaz
- **Email:** oscarpiediaz@gmail.com
- **GitHub:** https://github.com/oHastee

