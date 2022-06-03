# Basic program for calculations
# Ask the user for the amount and the price, then uses this information to
# work out the price per unit


# Float checker from 01_user_budget_trial3_v2
def float_checker(question):
    number = ""
    while not number:
        try:
            number = float(input(question))
            return number
        except ValueError:
            print("Please enter a valid float (i.e. number can include "
                  "decimals)")


# Basic program for calculations
amount = float_checker("Number of units: ")
price = float_checker("Enter price: $")
price_per_unit = price / amount
print(f"The price per unit = ${price_per_unit:,.3f}")
