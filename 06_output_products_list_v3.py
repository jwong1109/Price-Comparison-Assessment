# All the outputting details together
# Adjusted the format for the output of the cheapest and most expensive

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
    if not product[2] > budget:  # if the original cost is less than the budget
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

# Another unit_prices_list to find the average
unit_prices_list = []

for product in details:
    unit_price = product[3]
    unit_prices_list.append(unit_price)

average = sum(unit_prices_list)/len(unit_prices_list)
print(f"The AVERAGE unit price is ${average:,.3f} per {unit_choice}\n")

# Cheapest Product
cheapest_product_details = details[0]
cheapest_name = cheapest_product_details[0]
cheapest_unit_price = cheapest_product_details[3]
print(f"The CHEAPEST product based on unit price:")
print(f"Product Name: {cheapest_name}")
print(f"Unit Price: ${cheapest_unit_price:,.3f}\n")

# Most Expensive Product
most_expensive_product_details = details[-1]
most_expensive_name = most_expensive_product_details[0]
most_expensive_unit_price = most_expensive_product_details[3]
print(f"The MOST EXPENSIVE product based on unit price:")
print(f"Product Name: {most_expensive_name}")
print(f"Unit Price: ${most_expensive_unit_price:,.3f}\n")
