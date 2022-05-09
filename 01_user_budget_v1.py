# Float checker - first trial method
def float_checker(question, low_num, high_num):
    error = f"Please enter a budget that is between {low_num} and {high_num}"
    valid = False
    while not valid:
        # ask user for the budget and check its validity
        try:
            number_to_check = float(input(question))
            if low_num <= number_to_check <= high_num:
                return number_to_check
            else:
                print(error)
        except ValueError:
            print("\nPlease enter a valid float (i.e. number can include "
                  "decimals)")


# Main routine
budget = float_checker("\nPlease enter your budget: $", 1, 500)
print(f"Budget = ${budget}")
