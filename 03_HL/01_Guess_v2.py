# Functions at the top
def yes_no(question):
    while True:

        # Variables
        yes_variables = ["yes", "y", "yer", "yeah"]
        no_variables = ["no", "n", "nay"]
        # Ask the user if they have played before

        response = input(question).lower()

        # If they say yes, output 'program continues'
        if response.lower() in yes_variables:
            response = "yes"
            return response

        elif response.lower() in no_variables:
            response = "no"
            return response

        elif response.lower() == "xxx":
            break

        else:
            print("Please type either yes or no ")


def num_check(question, low=None, high=None):

    situation = ""

    if low is not None and high is not None:
        situation = "both"

    if low is not None and high is None:
        situation = "Low only"

    while True:

        try:
            # ask the question
            response = int(input(question))

            if situation == "both":
                if low > response or high < response:
                    print(f"Please enter a number between {low} and {high}")
                    continue
            elif situation == "Low only":
                if response < low:
                    print(f"Please enter a number that is more than (or equal to) {low}")
                    continue
            return response

        except ValueError:
            print("Please enter an integer")
            continue


# Main routine
default = yes_no("Would you like to use default settings? ")

if default == "yes":
    lowest = 1
    highest = 100
else:
    lowest = num_check("Low Number: ")
    highest = num_check("High Number: ", lowest + 1)

rounds = num_check("Rounds: ")

for i in range(rounds):
    guess = num_check("Guess: ", lowest, highest)
    print(f"You have guessed: {guess}")
