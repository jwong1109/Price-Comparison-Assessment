# Uses .isalpha() test to ensure name contain at least one letter.
# It won't accept spaces
# Simplify the while loop
# Created a variable for error message

# Check Product Name Function
def not_blank(question):
    error_message = "You can't leave this blank...\n"
    while True:
        response = input(question)
        if not response.isalpha():
            print(error_message)
        else:
            return response


# Main Routine
product_name = not_blank("Enter the product name for comparison: ")
