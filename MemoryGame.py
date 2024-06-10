import random
import time
import Score
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
        guess_number.append(int(input(f"What is your memorize number from 1 to 100:")))
        i = i + 1
    return guess_number


def compare_results(list_of_number, guess_number):
    comp=(list_of_number == guess_number)
    print(comp)
    return comp


def play(diff):
    x = generate_sequence(diff)
    # print the generated list for 0.7s and clear screen
    print(x, end='', flush=True)
    time.sleep(0.7)
    print("\r", end='', flush=True)  # This clears the printed text after the duration

    y = get_guess_from_user(diff)
    print(y)
    if compare_results(x, y):
        return True



# compare_results(x, y)
# play(5)