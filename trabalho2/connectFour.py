from tabuleiro import Tabuleiro

def makeMove(node: Tabuleiro, n: int, player:str):
    new_table = list(map(list, node.getGame()))
    n = n - 1
    if(node.getColumnsDone()[n]):
        print("Coluna escolhida está cheia!\n")
    for i in range(len(new_table)):
        if (new_table[i][n] !='-'):
            i = i - 1
            break
    if(player == 'BOT'):
        new_table[i][n] = 'O'
    else:
        new_table[i][n] = 'X'
    new_table = Tabuleiro(new_table)
    return new_table

def getActionsBot(node: Tabuleiro):
    actions = []
    for i in range(1,8,1):
        print(i)
        if(node.getColumnsDone()[i-1] is False):
            actions.append(makeMove(node,i, 'BOT'))
    for i in actions:
        print(i)
    return actions

tab = [
    ['X','-','-','-','-','-','X'],
    ['X','-','-','-','-','-','X'],
    ['X','-','-','-','-','-','X'],
    ['X','-','-','-','-','-','X'],
    ['X','-','-','-','-','-','X'],
    ['X','-','-','-','-','-','X']
]

tab = Tabuleiro(tab)
getActionsBot(tab)
# for i in getActionsBot(tab):
#     print(i)
# while(True):
#     print(tab)
#     play = int(input("Which column u want to put:\n1-7\n"))
#     tab = makeMove(tab, play, 'PLAYER')
# print(tab.getPoints())
# bot_plays = getActionsBot(tab)
# 


# while(True):
#     print(tab) 
#     play = int(input("Which column u want to put:\n1-7\n"))
#     tab = playerPlays(tab, play)
#     print(tab)

#     play = int(input("Which column u want to put:\n1-7\n"))
#     tab = playerPlays2(tab, play)