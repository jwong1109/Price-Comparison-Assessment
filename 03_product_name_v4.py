# While loop in the main routine
# Uses None to see whether the product_name is blank

# Check Product Name Function
def not_blank(question):
    response = input(question)
    if not response.isalpha():
        print("You can't leave this blank...\n")
    else:
        return response


# Main Routine
product_name = None
while product_name is None:
    product_name = not_blank("Enter the product name for comparison: ")
