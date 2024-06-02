import random


def generate_sequence(diff):
    list_of_number = []
    i = 0
    while i < diff:
        list_of_number.append(random.randint(1, 100))
        i = i + 1
    return list_of_number

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


print(generate_sequence(7))
