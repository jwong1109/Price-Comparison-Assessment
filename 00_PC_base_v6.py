# Added details list, append and sort methods from 05_append_details_list_v3

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
    chosen_unit = input("Enter a valid unit for comparison: ")
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
def calculate_price_per_unit():
    amount = float_checker("Number of units: ")
    price = float_checker("Enter price: $")
    price_per_unit_calculation = price / amount
    return price_per_unit_calculation


# ******** Main Routine ********

# Set up dictionaries / lists needed to hold data
details = []

# Ask user if they have used the program before and
# show instructions if needed

# Get user budget (between 1 and 500)
MINIMUM_BUDGET = 1
MAXIMUM_BUDGET = 500
budget = float_checker("\nPlease enter your budget: $")
while budget < MINIMUM_BUDGET:  # budget needs to be between 1 and 500
    budget = float_checker("Your budget needs to be at least $1!\n"
                           "\nPlease enter your budget: $")
while budget > MAXIMUM_BUDGET:
    budget = float_checker("The maximum budget you can have is $500!\n"
                           "\nPlease enter your budget: $")
print(f"Budget = ${budget:,.2f}")

# Get unit choice for comparison (mL, L, kg, g)
unit_choice = None
while unit_choice is None:
    unit_choice = get_unit()

print(f"Unit = {unit_choice}")

# Get input for product name
product_name = ""
while product_name != "X":  # Loop code to get various products
    product_name = not_blank("Enter the product name for comparison: ").title()
    if product_name != "X":
        print(f"Product Name: {product_name}\n")
        # Get input for the number of units (amount) and price
        price_per_unit = calculate_price_per_unit()
        # Calculate price per unit
        print(f"The price per unit = ${price_per_unit:,.3f}")
        # Append details to list and sort list to find cheapest
        entered_details = [product_name, f"${price_per_unit:,.3f}"]
        details.append(entered_details)

# Sort list and print the details
details.sort(key=lambda x: x[1])

# Output the products within and outside of the budget

# Present a recommendation
