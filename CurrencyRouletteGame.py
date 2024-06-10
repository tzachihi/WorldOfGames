import random
import requests
import Score
# self.api_url = "https://api.exchangerate-api.com/v4/latest/USD"  # Example API endpoint

def generate_number():
    return random.randint(1, 101)


def get_currency_rate():
    url = "https://api.exchangerate-api.com/v4/latest/USD"
    response = requests.get(url, verify=False)
    print(f'response is {response}')
    return response.json()['rates']['ILS']

def get_money_interval(diff, amount_in_usd):
    print(f'random number is {amount_in_usd}')
    rate = get_currency_rate()
    print(f'rate is {rate}')
    ils = int(rate * amount_in_usd)
    offset = 5 -diff
    return ils - offset, ils + offset

def get_guess_from_user(amount_in_usd):
    guess_money = (int(input(f"How much are {amount_in_usd} USD value in ILS:")))
    return guess_money

def compare_results(min_interval, gess, max_interval):
    comp = (min_interval <= gess <= max_interval)
    return comp

def play(diff):
    amount_in_usd = generate_number()
    min_interval, max_interval = get_money_interval(diff, amount_in_usd)
    print(f' min interval is {min_interval}, max interval is {max_interval}')
    gess = get_guess_from_user(amount_in_usd)
    print(gess)
    compare_results(min_interval, gess, max_interval)
    if compare_results(min_interval, gess, max_interval):
        return True


#play(5)
