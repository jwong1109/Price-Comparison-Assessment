# Ensures that a comment is made if there is a cheaper unit price outside
# the budget

# Also ensures that the correct phrase is used when describing how cheap the
# recommendation is.

# For testing purposes
budget = 3
unit_choice = "kg"
details = [["Cadbury", 180, 3.80, 0.021], ["Whittakers", 250, 5.50, 0.022],
           ["KitKat", 45, 1.00, 0.022]]
details.sort(key=lambda x: x[3])


# From 06_output_products_list_v5
# Processing products within and out of budget Function
def process_products():
    for each_item in details:
        if not each_item[2] > budget:  # if cost less than the budget
            # add it to in budget list
            products_in_budget.append(each_item)
        else:  # otherwise, for all other original cost greater than the budget
            # add it to out budget list
            products_out_budget.append(each_item)


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
    cheap_cost = cheapest_product_details[2]

    return cheapest_name, cheapest_unit_price, cheap_cost


# Main Routine
# From 06_output_products_list_v5
# Output products within and outside the budget
products_in_budget = []  # List to contain products in budget
products_out_budget = []  # List to contain products out of budget
process_products()

# Another unit_prices_list to find the average
unit_prices_list = []

average = average_unit_price()
# print(f"The AVERAGE unit price is ${average:,.3f} per {unit_choice}\n")

# Cheapest Product
# print(f"The CHEAPEST product based on unit price:")
cheap_details = cheapest_product()
# print(f"Product Name: {cheap_details[0]}")
# print(f"Unit Price: ${cheap_details[1]:,.3f}\n")

# Print Details List for testing purposes
print(details)
print()

# Recommendation
products_in_budget.sort(key=lambda x: x[3])
recommend_details = products_in_budget[0]
recommend_name = recommend_details[0]
recommend_amount = recommend_details[1]
recommend_cost = recommend_details[2]
recommend_unit_price = recommend_details[3]

if unit_prices_list[0] == recommend_unit_price:
    cheap = "the cheapest"
else:
    cheap = "a cheap"

print(f"We recommend that you purchase {recommend_name}.")
print(f"The cost of the recommended product is ${recommend_cost:,.2f} "
      f"for {recommend_amount}{unit_choice}.")
print(f"It is within your budget of ${budget:,.2f} and has {cheap} unit "
      f"price of ${recommend_unit_price:,.3f} per {unit_choice}. ")

if unit_prices_list[0] != recommend_unit_price:
    print(f"However, {cheap_details[0]} has a cheaper unit price of $"
          f"{cheap_details[1]:,.3f} per {unit_choice}, but the "
          f"cost price of {cheap_details[2]:,.2f} is over "
          f"your budget of ${budget:,.2f}. \nYou could consider increasing "
          f"your budget to purchase {cheap_details[0]}.")

