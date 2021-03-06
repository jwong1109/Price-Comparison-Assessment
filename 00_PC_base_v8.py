# Based on 00_PC_base_v7, I added 06_output_products_list_v5
# Also, adjusted minimum and maximum budget constants to print in the error
# messages
# Changed the entered_details list to containing only the variables itself

# Import Statements

# Functions go here


# Float Checker Function
def float_checker(question):
    number = ""
    while not number:
        # ask user for the budget and check its validity
        try:
            number = float(input(question))
            return number
        except ValueError:
            print("Please enter a valid float (i.e. number can include "
                  "decimals)")


# Unit comparison function
def get_unit():
    choice_error = "Sorry, please enter a valid unit (eg. mL, L, kg, g)\n "
    valid_units_list = [["mL", "ml", "millilitres", "1"], ["L", "litres", "2"],
                        ["kg", "kilograms", "3"], ["g", "grams", "4"]]
    chosen_unit = input("\nEnter a valid unit for comparison: ")
    for item in valid_units_list:
        if chosen_unit in item:
            return item[0]
    print(choice_error)


# Check Product Name Function
def not_blank(question):
    error_message = "You can't leave this blank...\n"
    while True:
        response = input(question)
        if not response.isalpha():
            print(error_message)
        else:
            return response


# Calculate price per unit function
def calculate_price_per_unit(entered_amount, entered_price):
    price_per_unit_calculation = entered_price / entered_amount
    return price_per_unit_calculation


# Processing products within and out of budget Function
def process_products():
    for each_item in all_details:
        if not each_item[2] > budget:  # if cost less than the budget
            # add it to in budget list
            products_in_budget.append(each_item)
        else:  # otherwise, for all other original cost greater than the budget
            # add it to out budget list
            products_out_budget.append(each_item)


# Printing products Function
def products_outputs(item):
    print(f"Product Name: {item[0]}")
    print(f"Amount: {item[1]}{unit_choice}")
    print(f"Cost Price: ${item[2]:,.2f}")
    print(f"Unit Price: ${item[3]:,.3f}\n")


# Average Unit Price Function
def average_unit_price():
    for product in all_details:
        unit_price = product[3]
        unit_prices_list.append(unit_price)

    calculate_average = sum(unit_prices_list)/len(unit_prices_list)
    return calculate_average


# Cheapest Product Function
def cheapest_product():
    cheapest_product_details = all_details[0]
    cheapest_name = cheapest_product_details[0]
    cheapest_unit_price = cheapest_product_details[3]

    return cheapest_name, cheapest_unit_price


# Most Expensive Product Function
def most_expensive_product():
    most_expensive_product_details = all_details[-1]
    most_expensive_name = most_expensive_product_details[0]
    most_expensive_unit_price = most_expensive_product_details[3]

    return most_expensive_name, most_expensive_unit_price


# ******** Main Routine ********

# Set up dictionaries / lists needed to hold data
all_details = []  # List to contain all the details
products_in_budget = []  # List to contain products in budget
products_out_budget = []  # List to contain products out of budget
unit_prices_list = []  # Another unit_prices_list to find the average

# Ask user if they have used the program before and
# show instructions if needed

# Get user budget (between 1 and 500)
MINIMUM_BUDGET = 1
MAXIMUM_BUDGET = 500
budget = float_checker("\nPlease enter your budget: $")
while budget < MINIMUM_BUDGET:  # budget needs to be between 1 and 500
    budget = float_checker(f"Your budget needs to be at least "
                           f"${MINIMUM_BUDGET}!\n"
                           "\nPlease enter your budget: $")
while budget > MAXIMUM_BUDGET:
    budget = float_checker(f"The maximum budget you can have is "
                           f"${MAXIMUM_BUDGET}!\n"
                           "\nPlease enter your budget: $")
print(f"Budget = ${budget:,.2f}")

# Get unit choice for comparison (mL, L, kg, g)
unit_choice = None
while unit_choice is None:
    unit_choice = get_unit()

print(f"Unit = {unit_choice}\n")

# Get input for product name
product_name = ""
while product_name != "X":  # Loop code to get various products
    product_name = not_blank("Enter the product name for comparison: ").title()
    if product_name != "X":
        print(f"Product Name: {product_name}\n")
        # Get input for the number of units (amount) and price
        amount = float_checker("Number of units: ")
        price = float_checker("Enter price: $")
        # Calculate price per unit
        price_per_unit = calculate_price_per_unit(amount, price)
        print(f"The price per unit = ${price_per_unit:,.3f}\n")
        # Append details to list and sort list to find cheapest
        entered_details = [product_name, amount, price, price_per_unit]
        all_details.append(entered_details)

# Sort list according to cheapest unit price first
all_details.sort(key=lambda x: x[3])

# Output the products within and outside of the budget
process_products()

# Print products within budget
if len(products_in_budget):
    print("The cost prices of the products that are within the budget are:\n")
    for each_product in products_in_budget:
        products_outputs(each_product)

# Print products outside of the budget
if len(products_out_budget):
    print("The cost prices of the products that are "
          "outside of the budget are:\n")
    for each_product in products_out_budget:
        products_outputs(each_product)

if len(all_details):
    # Average Unit Price
    average = average_unit_price()
    print(f"The AVERAGE unit price is ${average:,.3f} per {unit_choice}\n")

    # Cheapest Product
    print(f"The CHEAPEST product based on unit price:")
    cheap_details = cheapest_product()
    print(f"Product Name: {cheap_details[0]}")
    print(f"Unit Price: ${cheap_details[1]:,.3f}\n")

    # Most Expensive Product
    print(f"The MOST EXPENSIVE product based on unit price:")
    most_expensive_details = most_expensive_product()
    print(f"Product Name: {most_expensive_details[0]}")
    print(f"Unit Price: ${most_expensive_details[1]:,.3f}\n")

# Present a recommendation
