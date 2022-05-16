# Float checker - second trial method. Loops until a valid float is entered
# This version trials 'isinstance()' to confirm the float and has less
# parameters in the function since the valid budget range will loop in
# the main routine.

def float_checker(question):
    valid = False
    while not valid:
        # ask user for the budget and check its validity
        try:
            number_to_check = float(input(question))
            if isinstance(number_to_check, float):
                valid = True
                return number_to_check
        except ValueError:
            print("Please enter a valid float (i.e. number can include "
                  "decimals)")


# Main routine
# Check for an appropriate budget between 1 and 500
budget = float_checker("\nPlease enter your budget: $")
while budget < 1 or budget > 500:
    budget = float_checker("Please enter a budget that is between 1 and 500!\n"
                           "\nPlease enter your budget: $")

print(f"Budget = ${budget}")
