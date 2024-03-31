import random

def generate_number(difficulty):
    return random.randint(1,difficulty)

def get_guess_from_user(difficuly):
    while True:
        try:
            guess = int(input(f"Guess a number between 1 and {difficuly}"))
            if 1 <= guess <= difficuly:
                return guess
            else:
                print(f"please enter a number between 1 and{difficuly}")
        except ValueError:
            print("Please enter a valid number")
def compare_results(secret_number, guess):
    if guess == secret_number:
        print("Congratulations! you guessed the correct number")
        return True
    else:
        print(f"Wrong guess the correct number was: {secret_number}")
        return False

def play(difficulty):
    secret_number = generate_number(difficulty)
    guess = get_guess_from_user(difficulty)
    return compare_results(secret_number, guess)

