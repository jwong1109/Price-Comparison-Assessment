# Trial 2: Creating a checker to ensure that the product name is not blank
# Put error message in main routine as a second parameter for the function
# While loop in the main routine
# Uses None to see whether the product_name is blank
# Make the not_blank function more generic

# Check Product Name Function
def not_blank(question, error_message):
    response = input(question)
    if not response:
        print(error_message)
    else:
        return response


# Main Routine
product_name = None
while product_name is None:
    product_name = not_blank("Enter the product name for comparison: ",
                             "You can't leave this blank...\n")

