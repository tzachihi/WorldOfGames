from Live import load_game, welcome
import Score
import MainScores



print(welcome("Guy"))
load_game()
print(Score.read_score())
MainScores.worldOfGame()
