from minimax import play_min_max
from alphabeta import play_alpha_beta
from mcts import play_mcts
from tabuleiro import Tabuleiro

tab = [
    ['-','-','-','-','-','-','-'],
    ['-','-','-','-','-','-','-'],
    ['-','-','-','-','-','-','-'],
    ['-','-','-','-','-','-','-'],
    ['-','-','-','-','-','-','-'],
    ['-','-','-','-','-','-','-']
]
tab = Tabuleiro(tab)

def main():
    desired_game = int(input("Contra qual algoritmo deseja jogar?\n[1]: Minimax\n[2]: Alphabeta\n[3]: MCTS\n"))
    if(desired_game == 1):
        print("\n----------- INICIANDO JOGO -----------")
        print("Algotimo selecionado: MINIMAX\n")
        print(tab)
        print('\n')
        play_min_max(tab)
    elif(desired_game == 2):
        print("\n----------- INICIANDO JOGO -----------")
        print("Algotimo selecionado: ALPHA-BETA\n")
        print(tab)
        print('\n')
        play_alpha_beta(tab)
    elif(desired_game == 3):
        print("\n----------- INICIANDO JOGO -----------")
        print("Algotimo selecionado: MCTS\n")
        print(tab)
        print('\n')
        play_mcts(tab)
    else:
        main()

main()
