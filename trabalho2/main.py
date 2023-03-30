from minimax import play_min_max
from alphabeta import play_alpha_beta
from tabuleiro import Tabuleiro

tab = [
    ['-','-','-','-','-','-','-'],
    ['-','-','-','-','-','-','-'],
    ['-','-','-','-','-','-','-'],
    ['-','-','-','-','-','-','-'],
    ['-','-','-','-','-','-','-'],
    ['-','-','-','-','-','-','-']
]

desired_game = int(input("Contra qual algoritmo deseja jogar?\n[1]: Minimax\n[2]: Alphabeta\n[3]: MCTS\n"))
if(desired_game == 1):
    play_min_max(tab)
elif(desired_game == 2):
    play_alpha_beta(tab)