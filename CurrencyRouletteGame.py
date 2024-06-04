import random
rate = 4
def generate_money ():
    money = random.randint(1, 100)
    return money

def get_money_interval(total_money, diff):
    t = total_money
    d = diff
    solution = (t - (5 - d), t + (5 - d))
    return solution



def get_guess_from_user():
    guess_money = (int(input(f"What is your guess amount of money:")))
    return guess_money


def compare_results(gen_money, low_money, high_money):
    comp=(low_money <= gen_money <= high_money)
    print(comp)
    if comp:
        print("You win the game")
    else:
        print("You lost the game")



def play(diff):
    gen_money = generate_money()
    print(gen_money)
    total_money = get_guess_from_user()
    print(total_money)
    print(get_money_interval(total_money, diff))
    money_int = get_money_interval(total_money, diff)
    low_money, high_money = money_int
    print(low_money)
    print(high_money)
    compare_results(gen_money, low_money, high_money)



play(3)

#     x = generate_sequence(diff)
#     print(x)
#     y = get_guess_from_user(diff)
#     print(y)
#     compare_results(x, y)



