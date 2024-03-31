import random
import time

def generate_sequence(difficulty):
    return [random.randint(1, 101) for _ in range(difficulty)]

def get_list_from_user(difficulty):
    print("Remember the following numbers for 0.7 seconds:")
    sequence = generate_sequence(difficulty)
    print(sequence)
    time.sleep(0.7)
    print("\n" * 100)  # Clear console
    user_sequence = []
    for _ in range(difficulty):
        user_input = input("Enter a number: ")
        user_sequence.append(int(user_input))
    return sequence, user_sequence

def is_list_equal(list1, list2):
    return all(x == y for x, y in zip(list1, list2))

def play(difficulty):
    correct_sequence, user_sequence = get_list_from_user(difficulty)
    return is_list_equal(correct_sequence, user_sequence)

# Example usage
