import requests
import random

def get_money_interval(difficulty):
    url = "https://api.freecurrencyapi.com/v1/latest?apikey=fca_live_oXzOwCLXoWPWcmAu7oLCWFYRyNF4buu6drVwTTTT&currencies=ILS"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if 'data' in data and 'ILS' in data['data']:
            rate = data['data']['ILS']
            total_value = random.randint(1,100)
            interval = (total_value - (5-difficulty), total_value + (5 - difficulty))
            return interval, rate
        else:
            print("Failed to find exchange rate for USD to ILS.")
            return None, None
    else:
        print("failed to fetch exchange rate.")
        return None, None

def get_guess_from_user():
    while True:
        try:
            guess = float(input("Guess the value in ILS :"))
            return guess
        except ValueError:
            print("Please enter a valid number.")

def play(difficulty):
    interval, rate = get_money_interval(difficulty)
    if interval is not None and rate is not None:
        print(f"USD to ILS rate: {rate}")
        print(f"The number in dollars is: {interval}")
        guess = get_guess_from_user()
        if interval[0] <= guess <= interval[1]:
            print("Congratulations! You won.")
        else:
            print("Sorry you lost.")

    return False