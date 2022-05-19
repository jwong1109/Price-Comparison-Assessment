# Make the not_blank function more generic
# Put error message in main routine as a second parameter for the function

# Check Product Name Function
def not_blank(question, error_message):
    valid = ""
    while not valid:
        response = input(question)
        if not response:
            print(error_message)
        else:
            return response


# Main Routine
product_name = not_blank("Enter the product name for comparison: ",
                         "You can't leave this blank...\n")
