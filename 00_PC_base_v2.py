# Added 01_user_budget_trial3_v2

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


# ******** Main Routine ********

# Set up dictionaries / lists needed to hold data

# Ask user if they have used the program before and
# show instructions if needed

# Loop to get details

    # Get user budget (between 1 and 500)
    budget = float_checker("\nPlease enter your budget: $")
    while budget < MINIMUM_BUDGET:  # budget needs to be between 1 and 500
        budget = float_checker("Your budget needs to be at least $1!\n"
                               "\nPlease enter your budget: $")
    while budget > MAXIMUM_BUDGET:
        budget = float_checker("The maximum budget you can have is $500!\n"
                               "\nPlease enter your budget: $")
    print(f"Budget = ${budget:,.2f}")

    # Get unit choice for comparison (mL, L, kg, g)

    # Get input for product name

    # Get input for the number of units (amount) and price

    # Calculate price per unit

    # Append details to list and sort list to find cheapest in ascending order

# Output the products within and outside of the budget

# Present a recommendation
