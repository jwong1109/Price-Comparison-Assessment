# Trial 1: Make this unit comparison into a function
# Basically, putting the original version 2 into a function
# There is a while loop in the function to repeat the original question
# until a valid response is entered

# Unit comparison function
def get_unit():
    valid_units_list = [["mL", "ml", "millilitres", "1"], ["L", "litres", "2"],
                        ["kg", "kilograms", "3"], ["g", "grams", "4"]]
    valid = False
    while valid is False:
        unit_choice = input("Please enter a valid unit for comparison (eg. "
                            "mL, L, kg, g): ")
        for item in valid_units_list:
            if unit_choice in item:
                return item[0]


print(f"Unit = {get_unit()}")
