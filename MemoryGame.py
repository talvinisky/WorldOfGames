import random
import time
from Utils import Screen_cleaner
def generate_sequence(difficulty):
    return [random.randint(1, 101) for _ in range(difficulty)]
def get_list_from_user(difficulty):
    print("Remember the following numbers for 0.7 seconds:")
    sequence = generate_sequence(difficulty)
    print(sequence)
    time.sleep(0.7)
    Screen_cleaner() #clears console
    user_sequence = []
    for _ in range(difficulty):
        while True:
            try:
                user_input = input("Enter One number at a time: ")
                user_sequence.append(int(user_input))
                break  # Break the loop if input is successfully converted to an integer
            except ValueError:
                print("Please enter a valid integer.")
    return sequence, user_sequence

def is_list_equal(list1, list2):
    return all(x == y for x, y in zip(list1, list2))

def play(difficulty):
    correct_sequence, user_sequence = get_list_from_user(difficulty)
    if is_list_equal(correct_sequence, user_sequence):
        print("Congratulations! You guessed correctly.")
        return True
    else:
        print("Sorry, you guessed incorrectly.")
        return False



