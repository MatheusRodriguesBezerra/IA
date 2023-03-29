from minimax import play_min_max
from tabuleiro import Tabuleiro
# from alphabeta import play_alpha_beta

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

# tab = [
#     ['-', '-', 'X', '-', '-', '-', '-'],
#     ['-', '-', 'O', '-', '-', '-', '-'],
#     ['-', '-', 'O', 'O', '-', '-', '-'],
#     ['-', '-', 'O', 'X', 'O', '-', '-'],
#     ['-', '-', 'X', 'O', 'X', 'O', '-'],
#     ['X', 'O', 'X', 'X', 'X', 'O', 'X']
# ]
# tab = Tabuleiro(tab)
# print(tab.getPoints())