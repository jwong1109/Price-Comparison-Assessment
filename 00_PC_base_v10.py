# Based on 00_PC_base_v9, I added the instructions for the program from
# 08_instructions_v2
# Also, added a welcome statement at the start of the program

# Wrote comments throughout the entire program

# Import Statements

# Functions go here
# Function takes the entered choice and list of valid choices as parameters
def get_choice(choice, valid_choices):
    choice_error = "Sorry, that is not a valid choice"
    # for each list of a possible response in the valid choices list
    for list_item in valid_choices:
        # if the entered input is in the list of possible response
        if choice in list_item:
            choice = list_item[0].title()  # simplify the choice in
            # the list eg. yes becomes "Y"
            return choice  # return the choice to the main routine
    print(choice_error)  # if the response is invalid, print the error message


# Function containing instructions
def show_instructions(valid_responses):
    instructions = ""
    while not instructions:  # This loops until a valid response is entered
        instructions = not_blank("Would you like to read the instructions for "
                                 "this price comparison program?: ")
        instructions = (get_choice(instructions, valid_responses))

    if instructions == "Y":  # If the user wants to read the instructions
        # print the instructions
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

    # then, the program begins
    print("Program launches...")


# Float Checker Function
def float_checker(question):
    number = ""
    while not number:  # This loops until a valid float is entered
        # ask user for the budget and check its validity
        try:
            number = float(input(question))
            return number  # return the number if it is a float
        except ValueError:  # if a string is entered, print the following:
            print("Please enter a valid float (i.e. number can include "
                  "decimals)")


# Unit comparison function
def get_unit():
    choice_error = "Sorry, please enter a valid unit (eg. mL, L, kg, g)\n "
    # the valid units allowed for the unit choice
    valid_units_list = [["mL", "ml", "millilitres", "1"], ["L", "litres", "2"],
                        ["kg", "kilograms", "3"], ["g", "grams", "4"]]
    # Ask user to enter a valid unit for comparison
    chosen_unit = input("\nEnter a valid unit for comparison: ")
    # for each unit list in the overall valid_units_list
    for item in valid_units_list:
        # if the user input can be found in any unit list
        if chosen_unit in item:
            return item[0]  # return the initials of the unit
    print(choice_error)  # if unit is invalid, print the error message


# Check Product Name Function
def not_blank(question):
    error_message = "You can't leave this blank...\n"
    while True:  # This loops until a valid response is entered
        response = input(question)  # ask user for an input to the question
        # if the response is blank or a space is entered
        if not response.isalpha():
            print(error_message)  # print the error message
        else:  # otherwise
            return response  # return the valid response


# Calculate price per unit function
# The function takes two parameters of the quantity and cost of the product
def calculate_price_per_unit(entered_amount, entered_price):
    # Price per unit = cost/quantity
    price_per_unit_calculation = entered_price / entered_amount
    return price_per_unit_calculation  # return price_per_unit


# Processing products within and out of budget Function
def process_products():
    for each_item in all_details:  # for each product details list
        if not each_item[2] > budget:  # if cost less than the budget
            # add it to in budget list
            products_in_budget.append(each_item)
        else:  # otherwise, for all other original cost greater than the budget
            # add it to out budget list
            products_out_budget.append(each_item)


# Printing products Function
def products_outputs(item):
    # print the first detail (product name) for the product
    print(f"Product Name: {item[0]}")
    # print the second detail (amount) for the product with its chosen unit
    print(f"Amount: {item[1]}{unit_choice}")
    # print the third detail (cost price) with dollar sign and rounded to 2dp
    print(f"Cost Price: ${item[2]:,.2f}")
    # print the fourth detail (unit price) with dollar sign and rounded to 3dp
    print(f"Unit Price: ${item[3]:,.3f}\n")


# Average Unit Price Function
def average_unit_price():
    for product in all_details:  # for each product details list
        # the unit price of the product is the fourth detail in the list
        unit_price = product[3]
        # add the unit price of each product into a unit prices list
        unit_prices_list.append(unit_price)
    # then use the unit prices list to calculate average by adding the total
    # of all unit prices and dividing the total by the amount of items in
    # the list
    calculate_average = sum(unit_prices_list)/len(unit_prices_list)
    return calculate_average  # then return the calculated average


# Cheapest Product Function
def cheapest_product():
    # the cheapest product details is the first product details in the
    # sorted all details list
    cheapest_product_details = all_details[0]
    # cheapest name is the first item of the cheapest product details
    cheapest_name = cheapest_product_details[0]
    # cheapest unit price is the fourth item of the cheapest product details
    cheapest_unit_price = cheapest_product_details[3]
    # cheapest cost price is the third item of the cheapest product details
    cheap_cost = cheapest_product_details[2]
    # return the name, unit price, and cost for the cheapest product
    return cheapest_name, cheapest_unit_price, cheap_cost


# Most Expensive Product Function
def most_expensive_product():
    # the most expensive product details is the last product details in the
    # sorted all details list
    most_expensive_product_details = all_details[-1]
    # most expensive name is the first item of the most expensive product
    # details
    most_expensive_name = most_expensive_product_details[0]
    # most expensive name is the fourth item of the most expensive product
    # details
    most_expensive_unit_price = most_expensive_product_details[3]
    # return the name and the unit price for the most expensive product
    return most_expensive_name, most_expensive_unit_price


# Make Recommendation Function
def make_recommendation():
    # recommended details is the first product details in the sorted
    # products in budget list
    recommend_details = products_in_budget[0]
    # recommended name is the first item of the recommended product details
    recommend_name = recommend_details[0]
    # the quantity of the recommended product is the second item of the
    # recommended product details
    recommend_amount = recommend_details[1]
    # the cost price of the recommended product is the third item of the
    # recommended product details
    recommend_cost = recommend_details[2]
    # the unit price of the recommended product is the fourth item of the
    # recommended product details
    recommend_unit_price = recommend_details[3]

    # to find the phrase to describe how cheap the recommended product is
    how_cheap = decide_cheap(recommend_unit_price)

    # print the following written recommendation:
    print(f"We recommend that you purchase {recommend_name}.")
    print(f"The cost of the recommended product is ${recommend_cost:,.2f} "
          f"for {recommend_amount}{unit_choice}.")
    print(f"It is within your budget of ${budget:,.2f} and has "
          f"{how_cheap} unit price of "
          f"${recommend_unit_price:,.3f} per {unit_choice}. ")

    if unit_prices_list[0] != recommend_unit_price:  # if there is a
        # product with a cheaper unit price that is out of budget
        cheaper_out_of_budget()  # call the function that will comment on this


# Decide how cheap Function
def decide_cheap(recommend_cheap_price):
    if unit_prices_list[0] == recommend_cheap_price:  # if the recommended
        # product has the cheapest unit price
        cheap = "the cheapest"  # print in the recommendation that the
        # recommended product has the cheapest unit price
    else:  # otherwise, there is a cheaper unit price than the recommended one
        cheap = "a cheap"  # print in the recommendation that the
        # recommended product has a cheap unit price
    return cheap  # return the phrase to use when describing how cheap the
    # recommended product's unit price is


# Cheaper out of budget Function
def cheaper_out_of_budget():
    # if there is a cheaper unit price (out of budget) than the unit price of
    # the recommended product
    # cheap_details[0] = cheapest product name
    # cheap_details[1] = cheapest unit price
    # cheap_details[2] = the cost of the cheapest product based on unit price
    # print the following:
    print(f"\nHowever, {cheap_details[0]} has a cheaper unit price of $"
          f"{cheap_details[1]:,.3f} per {unit_choice}, but the "
          f"cost price of ${cheap_details[2]:,.2f} is over "
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

# Welcome the user
print("Welcome to your Price Comparison Tool!!")
show_instructions(valid_yes_no)  # call the function that ask user if they
# have used the program before and whether they would like to read the
# instructions

# Get user budget (between 1 and 500)
# Minimum budget = 1, users don't enter a negative budget
MINIMUM_BUDGET = 1
# Max budget = 500, in case users want to compare
# expensive products that need a high budget
MAXIMUM_BUDGET = 500

# Ask user about the budget - check that it is a float
budget = float_checker("\nPlease enter your budget: $")
while budget < MINIMUM_BUDGET:  # if budget is less than $1
    # print an error message that addresses the issue directly
    budget = float_checker(f"Your budget needs to be at least "
                           f"${MINIMUM_BUDGET}!\n"
                           "\nPlease enter your budget: $")
while budget > MAXIMUM_BUDGET:  # if budget is above $500
    # print an error message that addresses the issue directly
    budget = float_checker(f"The maximum budget you can have is "
                           f"${MAXIMUM_BUDGET}!\n"
                           "\nPlease enter your budget: $")
print(f"Budget = ${budget:,.2f}")  # Show the entered budget rounded to 2dp

# Get unit choice for comparison (mL, L, kg, g)
unit_choice = None
while unit_choice is None:  # while there is no valid unit choice entered
    unit_choice = get_unit()  # call the function to get unit choice

print(f"Unit = {unit_choice}\n")  # print the unit choice in its initials

# Get input for product name
product_name = ""
while product_name != "X":  # Loop code to get various products
    product_name = not_blank("Enter the product name for comparison: ").title()
    if product_name != "X":  # if a product name is entered
        # print the product name in with the first letter being capital
        print(f"Product Name: {product_name}\n")
        # Get input for the number of units (amount) and price - check it is
        # a float
        amount = float_checker("Number of units: ")
        price = float_checker("Enter price: $")
        # Calculate price per unit - call the function with amount and price
        # as two parameters
        price_per_unit = calculate_price_per_unit(amount, price)
        # print the price per unit rounded to 3dp
        print(f"The price per unit = ${price_per_unit:,.3f}\n")
        # Append all entered details as a list to the all_details list
        entered_details = [product_name, amount, price, price_per_unit]
        all_details.append(entered_details)

# Sort list according to cheapest unit price first
# (4th item in entered_details list)
all_details.sort(key=lambda x: x[3])

# Output the products within and outside of the budget
process_products()

# Print products within budget
if len(products_in_budget):  # if there are products within the budget,
    # then print the following
    print("The cost prices of the products that are within the budget are:\n")
    for each_product in products_in_budget:  # for each product details
        # with cost prices that are within the budget, call the function to
        # print the details of these products
        products_outputs(each_product)

# Print products outside of the budget
if len(products_out_budget):  # if there are products outside of the budget,
    # then print the following
    print("The cost prices of the products that are "
          "outside of the budget are:\n")
    for each_product in products_out_budget:  # for each product details
        # with cost prices that are outside of the budget, call the function
        # to print the details of these products
        products_outputs(each_product)

if len(all_details):  # only output this information if there is at least one
    # product
    # entered
    # Average Unit Price
    average = average_unit_price()
    print(f"The AVERAGE unit price is ${average:,.3f} per {unit_choice}\n")

    # Cheapest Product
    print(f"The CHEAPEST product based on unit price:")
    cheap_details = cheapest_product()
    print(f"Product Name: {cheap_details[0]}")  # print the first item
    # (product name) in the cheapest product details
    print(f"Unit Price: ${cheap_details[1]:,.3f}\n")  # print the second item
    # (unit price) in the cheapest product details rounded to 3dp

    # Most Expensive Product
    print(f"The MOST EXPENSIVE product based on unit price:")
    most_expensive_details = most_expensive_product()
    # print the first item (product name) in the most expensive product details
    print(f"Product Name: {most_expensive_details[0]}")
    # print the second item (unit price) in the most expensive product
    # details rounded to 3dp
    print(f"Unit Price: ${most_expensive_details[1]:,.3f}\n")

    # Present a recommendation
    # Recommendation
    products_in_budget.sort(key=lambda x: x[3])  # sort the products within
    # budget based their cheapest unit prices first
    make_recommendation()  # call the recommendation function
