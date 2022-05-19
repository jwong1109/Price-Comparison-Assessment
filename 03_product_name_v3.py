# Uses .isalpha() test to ensure name contain at least one letter.
# It won't accept spaces

# Check Product Name Function
def not_blank(question):
    while True:
        response = input(question)
        if not response.isalpha():
            print("You can't leave this blank...\n")
        else:
            return response


# Main Routine
product_name = not_blank("Enter the product name for comparison: ")
