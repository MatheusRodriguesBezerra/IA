from tabuleiro import Tabuleiro

def makeMove(node: Tabuleiro, n: int, player:str):
    new_table = list(map(list, node.getGame()))
    n = n - 1
    if(node.getColumnsDone()[n]):
        return None
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

def playerPlays(node: Tabuleiro):
    n = int(input("Em Qual coluna deseja jogar?\nR: "))
    print("----------- JOGADOR: "+ str(n) + " -----------")
    if(node.getColumnsDone()[n-1] is False):
        node = makeMove(node,n,'PLAYER')
        return node
    print("Coluna ja está cheia, escolha outra\n")
    return playerPlays(node)

def getActionsBot(node: Tabuleiro):
    actions = []
    for i in range(1,8,1):
        if(node.getColumnsDone()[i-1] is False):
            actions.append(makeMove(node,i, 'BOT'))
    return actions

def getActionsPlayer(node: Tabuleiro):
    actions = []
    for i in range(1,8,1):
        if(node.getColumnsDone()[i-1] is False):
            actions.append(makeMove(node,i, 'PLAYER'))
    return actions