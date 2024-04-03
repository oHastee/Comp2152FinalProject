from Expense_Category import ExpenseCategory

# Create instances of ExpenseCategory for each preset category
rent_category = ExpenseCategory("Rent")  # Expenses related to rent or mortgage payments
clothing_category = ExpenseCategory("Clothing")  # Expenses related to clothing purchases
investments_category = ExpenseCategory("Investments")  # Expenses related to investments and savings
utilities_category = ExpenseCategory("Utilities")  # Expenses related to utility bills (electricity, water, etc.)
transportation_category = ExpenseCategory("Transportation")  # Expenses related to transportation (fuel, public transit, etc.)
health_category = ExpenseCategory("Health")  # Expenses related to healthcare and medical expenses
education_category = ExpenseCategory("Education")  # Expenses related to education and learning
entertainment_category = ExpenseCategory("Entertainment")  # Expenses related to entertainment and leisure activities
travel_category = ExpenseCategory("Travel")  # Expenses related to travel (flights, accommodations, etc.)
personal_care_category = ExpenseCategory("Personal Care")  # Expenses related to personal care and grooming
gifts_category = ExpenseCategory("Gifts")  # Expenses related to gifts for others
home_maintenance_category = ExpenseCategory("Home Maintenance")  # Expenses related to home maintenance and repairs
charity_category = ExpenseCategory("Charity/Donations")  # Expenses related to charitable donations
groceries_category = ExpenseCategory("Groceries")  # Expenses related to grocery shopping
dining_out_category = ExpenseCategory("Dining Out")  # Expenses related to dining out at restaurants
subscriptions_category = ExpenseCategory("Subscriptions")  # Expenses related to subscription services
clothing_accessories_category = ExpenseCategory("Clothing & Accessories")  # Expenses related to clothing and accessories
pets_category = ExpenseCategory("Pets")  # Expenses related to pet care and supplies
home_decor_category = ExpenseCategory("Home Decor")  # Expenses related to home decor and furnishings

# Create a dictionary to store the preset ExpenseCategory objects
preset_categories = {
    "Rent": rent_category,
    "Clothing": clothing_category,
    "Investments": investments_category,
    "Utilities": utilities_category,
    "Transportation": transportation_category,
    "Health": health_category,
    "Education": education_category,
    "Entertainment": entertainment_category,
    "Travel": travel_category,
    "Personal Care": personal_care_category,
    "Gifts": gifts_category,
    "Home Maintenance": home_maintenance_category,
    "Charity/Donations": charity_category,
    "Groceries": groceries_category,
    "Dining Out": dining_out_category,
    "Subscriptions": subscriptions_category,
    "Clothing & Accessories": clothing_accessories_category,
    "Pets": pets_category,
    "Home Decor": home_decor_category
}
