# Trial 1: Creating a checker to ensure that the product name is not blank
# Uses 1 parameter (question) in the function
# While loop in the function

# Check Product Name Function
def not_blank(question):
    valid = ""
    while not valid:
        response = input(question)
        if not response:
            print("You can't leave this blank...\n")
        else:
            return response


# Main Routine
product_name = not_blank("Enter the product name for comparison: ")
