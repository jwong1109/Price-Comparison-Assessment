# Trial 2: Make this unit comparison into a function
# Removed the boolean of valid = False
# Only returns chosen_unit if in the valid list
# Otherwise, it will print the choice_error and returns None to represent the
# absence of a value. There is a while loop in the main routine to repeat the
# question until a valid response is entered

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


# Main Routine
unit_choice = None
while unit_choice is None:
    unit_choice = get_unit()

print(f"Unit = {unit_choice}")
