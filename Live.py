global difficulty, decision
from Score import add_score
from MemoryGame import play as play_memory_game
from GuessGame import play as play_guess_game
from CurrencyRouletteGame import play as play_currency_roulette_game
from Score import add_name
def welcome(name):
    print(f"Hello {name} and welcome to the World of games(WoG).")
    print("Here you can find many cool games to play")
    add_name(name)


def load_game():
    while True:
        print("""Please choose a game to play:
    1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back
    2. Guess Game - guess a number and see if you chose like the computer
    3. Currency Roulette - try and guess the value of a random amount of USD in ILS""")
        try:
            decision = int(input("Please insert a number between 1 - 3: "))
            while not 1 <= decision <= 3:
                decision = int(input("Please insert a number between 1 - 3: "))

            difficulty = int(input('Please choose game difficulty from 1 to 5:'))
            while not 1 <= difficulty <= 5:
                difficulty = int(input("Please insert a number between 1 - 5: "))
        except ValueError:
            print("Error: Enter just numbers please, not letters, words, etc...")
            continue

        if decision == 1:
            if bool(play_memory_game(difficulty)) is True:
                add_score(difficulty=difficulty)
        elif decision == 2:
            if bool(play_guess_game(difficulty)) is True:
                add_score(difficulty=difficulty)
        elif decision == 3:
            if bool(play_currency_roulette_game(difficulty)) is True:
                add_score(difficulty=difficulty)

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break

    return difficulty, decision






