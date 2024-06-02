from pathlib import Path

#A function i added to display the name of the user that plays the game

def add_name(name):
    try:
        # Try to open the file in append mode
        with open(Path("Scores.txt"), "a") as score_file:
            score_file.write(f"{name}\n")  # Write the name followed by a newline character
    except FileNotFoundError:
        # If the file doesn't exist, create it and write the name
        with open(Path("Scores.txt"), "w") as score_file:
            score_file.write(f"{name}\n")


# def add_score(difficulty):
#     POINTS_OF_WINNING = str((difficulty * 3) + 5)
#     # The function will read the current score in the scores file,
#     # if it fails it will create a new one and will save the current score.
#     try:
#         score_file_name = open(Path("Scores.txt"), "r")
#         score = open(Path("Scores.txt"), "a")
#         score.write(f" ,{POINTS_OF_WINNING}")
#     except FileNotFoundError:
#         score = open(Path("Scores.txt"), "x")
#         score.write(POINTS_OF_WINNING)
def add_score(difficulty):
    POINTS_OF_WINNING = str((difficulty * 3) + 5)
    # The function will read the current score in the scores file,
    # if it fails it will create a new one and will save the current score.
    try:
        # Open the Scores.txt file for appending
        with open(Path("Scores.txt"), "a") as score_file:
            # Write the new score on a new line
            score_file.write(POINTS_OF_WINNING + '\n')
    except FileNotFoundError:
        # If the file doesn't exist, create it and write the score
        with open(Path("Scores.txt"), "w") as score_file:
            score_file.write(POINTS_OF_WINNING + '\n')