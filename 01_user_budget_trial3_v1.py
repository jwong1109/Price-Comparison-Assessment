# Float checker - third trial
# Simplifies try/except by no longer using valid as a variable.
# Created BUDGET_RANGE as a constant instead and see whether entered input
# is in the budget range

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
BUDGET_RANGE = range(1, 501)  # between 1 and 500 inclusive
budget = float_checker("\nPlease enter your budget: $")
while budget not in BUDGET_RANGE:  # budget needs to be between 1 and 500
    budget = float_checker("Please enter a budget that is between 1 and 500!\n"
                           "\nPlease enter your budget: $")

print(f"Budget = ${budget}")
