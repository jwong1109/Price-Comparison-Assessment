# Float checker - developed from v3
# Separate the BUDGET_RANGE into two constants - minimum and maximum
# Specific messages directed towards the input entered
# Amounts rounded tidily to 2dp.

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


# Main routine
# Check for an appropriate budget between 1 and 500
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
