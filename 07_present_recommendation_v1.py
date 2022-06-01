# Present a recommendation with the cheapest unit price that is within
# budget

# For testing purposes
budget = 20
unit_choice = "kg"
details = [["Surf", 5, 12.00, 2.400], ["Earthon", 7.5, 58.29, 7.772],
           ["Yours", 0.95, 19.95, 21.000]]
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


# Main Routine
# From 06_output_products_list_v5
# Output products within and outside the budget
products_in_budget = []  # List to contain products in budget
products_out_budget = []  # List to contain products out of budget
process_products()

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
print(f"We recommend that you purchase {recommend_name}.")
print(f"The cost of the recommended product is ${recommend_cost:,.2f} "
      f"for {recommend_amount}{unit_choice}.")
print(f"It is within your budget of ${budget:,.2f} and has the cheapest unit "
      f"price of ${recommend_unit_price:,.3f} per {unit_choice}. ")

