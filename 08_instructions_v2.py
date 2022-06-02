# Based on 08_instructions_v1, this component is in it's own function and
# includes actual instructions

# Check Product Name Function
def not_blank(question):
    error_message = "You can't leave this blank...\n"
    while True:
        response = input(question)
        if not response.isalpha():
            print(error_message)
        else:
            return response


# Function takes the entered choice and list of valid choices as parameters
def get_choice(choice, valid_choices):
    choice_error = "Sorry, that is not a valid choice"
    for list_item in valid_choices:
        if choice in list_item:
            choice = list_item[0].title()
            return choice
    print(choice_error)


# Function containing instructions
def show_instructions(valid_responses):
    instructions = ""
    while not instructions:
        instructions = not_blank("Would you like to read the instructions for "
                                 "this price comparison program?: ")
        instructions = (get_choice(instructions, valid_responses))

    if instructions == "Y":
        print("\n**** Price Comparison Tool Instructions ****\n"
              "The purpose of this program is to help you compare the price "
              "of various products by comparing the unit price for each "
              "product. \nYou will first be asked to enter the maximum amount "
              "you want to spend on the product. \nOur "
              "recommended product will not be over your set budget. \nYou "
              "can enter in as many products you would like to compare. \nFor "
              "each product, we will ask you for its name, its mass/volume, "
              "and its original cost price. \nAfter you enter x for the "
              "product name, we will show you which items are within and "
              "outside of your budget. \nWe will also show you the cheapest "
              "and most expensive item based on unit price. \nFinally, "
              "we'll make a recommendation on which item you should be "
              "purchased.\n")

    print("Program launches...")


# Main Routine
# Valid options for any yes/no questions
valid_yes_no = [["y", "yes"], ["n", "no"]]
show_instructions(valid_yes_no)


