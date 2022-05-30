# Adding the sort method for the list from 05_append_details_list_v2

# From 04_calculate_price_per_unit_v2
# Calculate price per unit function
def calculate_price_per_unit():
    amount = float(input("Number of units: "))
    price = float(input("Enter price: $"))
    price_per_unit_calculation = price / amount
    return price_per_unit_calculation


# Main Routine
details = []


# Unit for comparison
unit = input("Enter unit: ")
print(f"Unit = {unit}")  # For testing purposes

# From 00_PC_base_v5:
# Get input for product name
product_name = ""
while product_name != "X":  # Loop code to get various products
    product_name = input("\nEnter the product name for comparison: ").title()
    if product_name != "X":
        print(f"Product Name: {product_name}\n")
        # Get input for the number of units (amount) and price
        price_per_unit = calculate_price_per_unit()
        # Calculate price per unit
        print(f"The price per unit = ${price_per_unit:,.3f}")

        # Append details to list and sort list to find cheapest
        entered_details = [product_name, f"${price_per_unit:,.3f}"]
        details.append(entered_details)

# Sort list and print the details
details.sort(key=lambda x: x[1])
for products in details:
    print(products)  # for testing purposes
