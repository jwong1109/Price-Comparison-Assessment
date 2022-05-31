# Finding the average unit price, the cheapest product, and the most
# expensive product from the list

# For testing purposes
budget = 20
unit_choice = "kg"
details = [["Surf", 5, 12.00, 2.400], ["Earthon", 7.5, 58.29, 7.772],
           ["Yours", 0.95, 19.95, 21.000]]
details.sort(key=lambda x: x[3])

# Another unit_prices_list to find the average
unit_prices_list = []

for product in details:
    unit_price = product[3]
    unit_prices_list.append(unit_price)

average = sum(unit_prices_list)/len(unit_prices_list)
print(f"The average unit price is ${average:,.3f} per {unit_choice}")

# Cheapest Product
cheapest_product_details = details[0]
cheapest_name = cheapest_product_details[0]
cheapest_unit_price = cheapest_product_details[3]
print(f"The cheapest product based on unit price is {cheapest_name} for "
      f"${cheapest_unit_price:,.3f}")

# Most Expensive Product
most_expensive_product_details = details[-1]
most_expensive_name = most_expensive_product_details[0]
most_expensive_unit_price = most_expensive_product_details[3]
print(f"The most expensive product based on unit price is "
      f"{most_expensive_name} for ${most_expensive_unit_price:,.3f}")
