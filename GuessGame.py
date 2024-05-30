import random


def generate_number(diff):
    secret = random.randint(1, diff)
    return secret

def get_guess_from_user(diff):
    guess = int(input(f"What is your guess number from 1 to {diff}:"))
    return guess


def compare_results(guess,secret):
    comp=(guess == secret)
    print(comp)


def play(diff):
    x = generate_number(diff)
    print(x)
    y = get_guess_from_user(diff)
    print(y)
    compare_results(x, y)

play(7)



