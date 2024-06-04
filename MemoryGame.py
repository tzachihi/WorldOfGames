import random
diff=5

def generate_sequence(diff):
    list_of_number = []
    i = 0
    while i < diff:
        list_of_number.append(random.randint(1, 100))
        i = i + 1
    return list_of_number

def get_guess_from_user(diff):
    guess_number = []
    i = 0
    while i < diff:
        guess_number.append(int(input(f"What is your guess number from 1 to {diff}:")))
        i = i + 1
    return guess_number


def compare_results(list_of_number, guess_number):
    comp=(list_of_number == guess_number)
    print(comp)


def play(diff):
    x = generate_number(diff)
    print(x)
    y = get_guess_from_user(diff)
    print(y)
    compare_results(x, y)


x = (generate_sequence(diff))
print(x)
y = (get_guess_from_user(diff))
print(x)
print(y)

compare_results(x, y)