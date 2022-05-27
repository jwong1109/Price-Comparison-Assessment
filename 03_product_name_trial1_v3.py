# Loop code to allow for multiple products to be entered
# Ensures that the product name is capitalised

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
product_name = ""
while product_name != "X":
    product_name = not_blank("Enter the product name for comparison: ").title()
    if product_name != "X":
        print(f"Product Name: {product_name}\n")
