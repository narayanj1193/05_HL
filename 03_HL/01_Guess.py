# Functions at the top
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
lowest = num_check("Low Number: ")
highest = num_check("High Number: ", lowest + 1)
rounds = num_check("Rounds: ")
print()

for i in range(rounds):
    guess = num_check("Guess: ", lowest, highest)
    print(f"You have guessed: {guess}")
