import random
import requests
def get_money_interval(total_value, difficulty):
    url = "https://api.freecurrencyapi.com/v1/latest?apikey=fca_live_oXzOwCLXoWPWcmAu7oLCWFYRyNF4buu6drVwTTTT&currencies=ILS"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if 'data' in data and 'ILS' in data['data']:
            rate = data['data']['ILS']
            lower_bound = total_value - (5 - difficulty)
            upper_bound = total_value + (5 - difficulty)
            interval = (lower_bound * rate, upper_bound * rate)
            return interval, rate
        else:
            print("Failed to find exchange rate for USD to ILS.")
            return None, None
    else:
        print("Failed to fetch exchange rate.")
        return None, None


def get_guess_from_user():
    while True:
        try:
            guess = float(input("Guess the value in ILS: "))
            return guess
        except ValueError:
            print("Please enter a valid number.")


def play(difficulty):
    total_value = random.randint(1, 100)
    interval, rate = get_money_interval(total_value, difficulty)
    if interval is not None and rate is not None:
        print(f"The random number generated in USD is: {total_value}")
        #shekels_value = total_value * rate /gets the amount in shekel value
        # the line below is to see the amount in shekels(used for testing edge cases)

        # print(f"The amount in shekels is: {shekels_value:.2f} ILS")

        # the line below is to see the the interval (used for testing edge cases)

        # print(f"The interval in ILS is: {interval[0]:.2f} - {interval[1]:.2f}")

        print(f"The current exchange rate is: 1 USD = {rate:.2f} ILS")
        guess = get_guess_from_user()
        if interval[0] <= guess <= interval[1]:
            print("Congratulations! You won.")
            return True
        else:
            print("Sorry, you lost.")
            return False


