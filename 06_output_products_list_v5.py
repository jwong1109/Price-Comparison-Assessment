# Ensures tht the outputs will only be printed if it is necessary
# If there are no costs within or outside of the budget, it won't print
# those statements

# For testing purposes
budget = 20
unit_choice = "kg"
details = [["Surf", 5, 12.00, 2.400], ["Earthon", 7.5, 58.29, 7.772],
           ["Yours", 0.95, 19.95, 21.000]]
details.sort(key=lambda x: x[3])


# Processing products within and out of budget Function
def process_products():
    for each_item in details:
        if not each_item[2] > budget:  # if cost less than the budget
            # add it to in budget list
            products_in_budget.append(each_item)
        else:  # otherwise, for all other original cost greater than the budget
            # add it to out budget list
            products_out_budget.append(each_item)


# Printing products Function
def products_outputs(item):
    print(f"Product Name: {item[0]}")
    print(f"Amount: {item[1]}{unit_choice}")
    print(f"Cost Price: ${item[2]:,.2f}")
    print(f"Unit Price: ${item[3]:,.3f}\n")


# Average Unit Price Function
def average_unit_price():
    for product in details:
        unit_price = product[3]
        unit_prices_list.append(unit_price)

    calculate_average = sum(unit_prices_list)/len(unit_prices_list)
    return calculate_average


# Cheapest Product Function
def cheapest_product():
    cheapest_product_details = details[0]
    cheapest_name = cheapest_product_details[0]
    cheapest_unit_price = cheapest_product_details[3]

    return cheapest_name, cheapest_unit_price


# Most Expensive Product Function
def most_expensive_product():
    most_expensive_product_details = details[-1]
    most_expensive_name = most_expensive_product_details[0]
    most_expensive_unit_price = most_expensive_product_details[3]

    return most_expensive_name, most_expensive_unit_price


# Main Routine

# Output products within and outside the budget
products_in_budget = []  # List to contain products in budget
products_out_budget = []  # List to contain products out of budget
process_products()

# Print products within budget
if len(products_in_budget):
    print("The cost prices of the products that are within the budget are:\n")
    for each_product in products_in_budget:
        products_outputs(each_product)

# Print products outside of the budget
if len(products_out_budget):
    print("The cost prices of the products that are outside of "
          "the budget are:\n")
    for each_product in products_out_budget:
        products_outputs(each_product)

# Another unit_prices_list to find the average
unit_prices_list = []

if len(details):
    average = average_unit_price()
    print(f"The AVERAGE unit price is ${average:,.3f} per {unit_choice}\n")

    # Cheapest Product
    print(f"The CHEAPEST product based on unit price:")
    cheap_details = cheapest_product()
    print(f"Product Name: {cheap_details[0]}")
    print(f"Unit Price: ${cheap_details[1]:,.3f}\n")

    # Most Expensive Product
    print(f"The MOST EXPENSIVE product based on unit price:")
    most_expensive_details = most_expensive_product()
    print(f"Product Name: {most_expensive_details[0]}")
    print(f"Unit Price: ${most_expensive_details[1]:,.3f}\n")
