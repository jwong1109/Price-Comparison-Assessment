# Allow for various valid inputs for the units

valid_units_list = [["mL", "ml", "millilitres", "1"], ["L", "litres", "2"],
                    ["kg", "kilograms", "3"], ["g", "grams", "4"]]
valid = False
while valid is False:
    unit_choice = input("Enter a valid unit for comparison (eg. mL, "
                        "L, kg, g): ")
    for item in valid_units_list:
        if unit_choice in item:
            print(f"Unit = {item[0]}")
            valid = True
