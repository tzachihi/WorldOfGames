import random


def generate_number(diff):
    secret = random.randint(1, diff)
    return secret

def get_guess_from_user(diff):
    return 0


def compare_results(guess,secret):
     return 0


def play(diff):
    x = generate_number(diff)
    print(x)

play(7)



