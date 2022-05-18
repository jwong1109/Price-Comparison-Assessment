# Basic checker for the initials of units

valid_units = ["mL", "L", "kg", "g"]
unit = input("Enter your units for comparison: ")

if unit in valid_units:
    print(f"Unit = {unit}")
else:
    print("Please enter a valid unit for comparison (eg. mL, L, kg, g)")
