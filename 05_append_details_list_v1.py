# Appending the details of each product into a details list

# From 04_calculate_price_per_unit_v2
# Calculate price per unit function
def calculate_price_per_unit():
    amount = float(input("Number of units: "))
    price = float(input("Enter price: $"))
    price_per_unit_calculation = price / amount
    return price_per_unit_calculation


# Main Routine
details = []

# From 00_PC_base_v5:
# Unit for comparison
print("Unit = g")  # For testing purposes

# Get input for product name
product_name = ""
while product_name != "X":  # Loop code to get various products
    product_name = input("\nEnter the product name for comparison: ").title()
    if product_name != "X":
        print(f"Product Name: {product_name}\n")
        # Get input for the number of units (amount) and price
        price_per_unit = calculate_price_per_unit()
        # Calculate price per unit
        print(f"The price per unit = ${price_per_unit:,.3f}\n")
        # Append details to list and sort list to find cheapest
        entered_details = f"{product_name}, {price_per_unit:,.3f}"
        details.append(entered_details)

        print(details)  # For testing purposes
