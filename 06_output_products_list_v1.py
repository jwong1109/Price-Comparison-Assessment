# Output the details of products within and outside the budget

# For testing purposes
budget = 20
unit_choice = "kg"
details = [["Surf", 5, 12.00, 2.400], ["Earthon", 7.5, 58.29, 7.772],
           ["Yours", 0.95, 19.95, 21.000]]
details.sort(key=lambda x: x[3])

# Output products within and outside the budget
products_in_budget = []  # List to contain products in budget
products_out_budget = []  # List to contain products out of budget
for product in details:
    if product[2] <= budget:  # if the original cost is less than the budget
        products_in_budget.append(product)  # add it to the in budget list
    else:  # otherwise, for all other original cost greater than the budget
        products_out_budget.append(product)  # add it to the out budget list

# Print products within budget
print("The cost prices of the products that are within the budget are:\n")
for product in products_in_budget:
    print(f"Product Name: {product[0]}")
    print(f"Amount: {product[1]}{unit_choice}")
    print(f"Cost Price: ${product[2]:,.2f}")
    print(f"Unit Price: ${product[3]:,.3f}\n")

# Print products outside of the budget
print("The cost prices of the products that are outside of the budget are:\n")
for product in products_out_budget:
    print(f"Product Name: {product[0]}")
    print(f"Amount: {product[1]}{unit_choice}")
    print(f"Cost Price: ${product[2]:,.2f}")
    print(f"Unit Price: ${product[3]:,.3f}\n")
