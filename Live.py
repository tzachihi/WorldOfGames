def welcome(name):
    msg = f"""
         Hello {name} and welcome to the World of Games (WoG).
         Here you can find many cool games to play.
         """
    return msg


def load_game():
    msg = """
        Please choose a game to play:
        1. Memory Game - a sequence of numbers will appear for 1 second and you have to
        guess it back
        2. Guess Game - guess a number and see if you chose like the computer
        3. Currency Roulette - try and guess the value of a random amount of USD in ILS
        """
    game = input(msg)

    diff = input("Please choose game difficulty from 1 to 5:")