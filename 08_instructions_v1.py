# This component allows new users to see the instructions if it is their
# first time using this program

# Created a function that takes the entered choice and list of valid choices
# as parameters for yes/no questions

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
def show_instructions():
    print("**** Price Comparison Tool Instructions ****\n"
          "Instructions go here. They are brief but helpful\n")


# Main Routine
# Valid options for any yes/no questions
valid_yes_no = [["y", "yes"], ["n", "no"]]

instructions = ""
while not instructions:
    instructions = not_blank("Would you like to read the instructions for "
                             "this price comparison program?: ")
    instructions = (get_choice(instructions, valid_yes_no))

if instructions == "Y":
    show_instructions()

print("Program launches...")
