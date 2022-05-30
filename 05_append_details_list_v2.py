# Sorting a given list into ascending order based on cheapest price


# Main Routine

# Details list for testing purposes
details = [["Greggs", 0.035], ["Moccona", 0.117], ["Nescafe", 0.043]]
details.sort(key=lambda x: x[1])

for products in details:
    print(products)
