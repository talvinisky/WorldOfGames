from GuessGame import play as play_guess_game
from MemoryGame import play as play_memory_game
from CurrencyRouletteGame import play as play_currency_roulette_game
def welcome(name):
    print(f"Hello {name} and welcome to the World of games(WoG).")
    print("Here you can find many cool games to play")
def load_game():
    print("Please chose a game to play:")
    print("1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back")
    print("2. Guess Game - guess a number and see if you chose like the computer")
    print("3. Currency Roulette - try and guess the value of a random amount of USD in ILS")
    num = int(input("Please make your selection:"))
    if 0 < num < 4:
        difficulty = int(input("Please choose game difficulty from 1 to 5:"))
        if 0 < difficulty < 6:
            if num == 1:
                play_guess_game(difficulty)
            if num == 2:
                result = play_memory_game(difficulty)
                if result:
                    print("congratulations you won")
                else:
                    print("sorry you lost")
            if num == 3:
                play_currency_roulette_game(difficulty)
        else:
            print("Enter a valid number of difficulty ")

    else:
        print("Enter a correct number ")





