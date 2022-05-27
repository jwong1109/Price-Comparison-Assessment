# Make the price per unit calculation into a function


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


# Calculate price per unit function
def calculate_price_per_unit():
    amount = float_checker("Number of units: ")
    price = float_checker("Enter price: $")
    price_per_unit_calculation = price / amount
    return price_per_unit_calculation


# Price per unit calculations
price_per_unit = calculate_price_per_unit()
print(f"The price per unit = ${price_per_unit:,.3f}")
