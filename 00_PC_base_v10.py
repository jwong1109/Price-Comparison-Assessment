# Based on 00_PC_base_v9, I added the instructions for the program from
# 08_instructions_v2
# Also, added a welcome statement at the start of the program

# Import Statements

# Functions go here
# Function takes the entered choice and list of valid choices as parameters
def get_choice(choice, valid_choices):
    choice_error = "Sorry, that is not a valid choice"
    for list_item in valid_choices:
        if choice in list_item:
            choice = list_item[0].title()
            return choice
    print(choice_error)


# Function containing instructions
def show_instructions(valid_responses):
    instructions = ""
    while not instructions:
        instructions = not_blank("Would you like to read the instructions for "
                                 "this price comparison program?: ")
        instructions = (get_choice(instructions, valid_responses))

    if instructions == "Y":
        print("\n**** Price Comparison Tool Instructions ****\n"
              "The purpose of this program is to help you compare the price "
              "of various products by comparing the unit price for each "
              "product. \nYou will first be asked to enter the maximum amount "
              "you want to spend on the product. \nOur "
              "recommended product will not be over your set budget. \nYou "
              "can enter in as many products you would like to compare. \nFor "
              "each product, we will ask you for its name, its mass/volume, "
              "and its original cost price. \nAfter you enter x for the "
              "product name, we will show you which items are within and "
              "outside of your budget. \nWe will also show you the cheapest "
              "and most expensive item based on unit price. \nFinally, "
              "we'll make a recommendation on which item you should be "
              "purchased.\n")

    print("Program launches...")


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


# Make Recommendation Function
def make_recommendation():
    recommend_details = products_in_budget[0]
    recommend_name = recommend_details[0]
    recommend_amount = recommend_details[1]
    recommend_cost = recommend_details[2]
    recommend_unit_price = recommend_details[3]

    how_cheap = decide_cheap(recommend_unit_price)

    print(f"We recommend that you purchase {recommend_name}.")
    print(f"The cost of the recommended product is ${recommend_cost:,.2f} "
          f"for {recommend_amount}{unit_choice}.")
    print(f"It is within your budget of ${budget:,.2f} and has {how_cheap} unit "
          f"price of ${recommend_unit_price:,.3f} per {unit_choice}. ")

    if unit_prices_list[0] != recommend_unit_price:
        cheaper_out_of_budget()


# Decide how cheap Function
def decide_cheap(recommend_cheap_price):
    if unit_prices_list[0] == recommend_cheap_price:
        cheap = "the cheapest"
    else:
        cheap = "a cheap"

    return cheap


# Cheaper out of budget Function
def cheaper_out_of_budget():
    print(f"\nHowever, {cheap_details[0]} has a cheaper unit price of $"
          f"{cheap_details[1]:,.3f} per {unit_choice}, but the "
          f"cost price of {cheap_details[2]:,.2f} is over "
          f"your budget of ${budget:,.2f}. \nYou could consider increasing "
          f"your budget to purchase {cheap_details[0]}.")


# ******** Main Routine ********

# Set up dictionaries / lists needed to hold data
all_details = []  # List to contain all the details
products_in_budget = []  # List to contain products in budget
products_out_budget = []  # List to contain products out of budget
unit_prices_list = []  # Another unit_prices_list to find the average
# A list of valid responses for yes and no answers
valid_yes_no = [["y", "yes"], ["n", "no"]]

# Welcome the user, ask user if they have used the program before and
# show instructions if needed
print("Welcome to your Price Comparison Tool!!")
show_instructions(valid_yes_no)

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
    # Recommendation
    products_in_budget.sort(key=lambda x: x[3])
    make_recommendation()
