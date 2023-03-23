from tabuleiro import Tabuleiro
from connectFour import getActionsBot, getActionsPlayer,playerPlays

def min_max_decision(board:Tabuleiro) -> Tabuleiro:
    current_value = -10000
    children = getActionsBot(board)
    play = board
    for i in range(len(children)):
        x = minValue(children[i], 1 , 3)
        if(x > current_value):
            current_value = x
            play = children[i]
    return play
    # max_v = maxValue(board, 0, 2)
    # return max_v

def maxValue(node:Tabuleiro, depth:int, limit:int):
    # print(node)
    if(node.gameOver()):
        return node.getPoints() + limit - depth
    if(depth<limit): 
        current_value = -10000
        children = getActionsBot(node)
        for i in range(len(children)):
            x = minValue(children[i], depth+1 , limit)
            if(x > current_value):
                current_value = x
        return current_value
    return node.getPoints()

def minValue(node:Tabuleiro, depth:int, limit:int): 
    if(node.gameOver()):
        return node.getPoints() + limit - depth
    
    if(depth<limit): 
        current_value = 10000
        children = getActionsPlayer(node)
        for i in range(len(children)):
            x = maxValue(children[i], depth+1 , limit)
            if(x<current_value):
                current_value = x
        return current_value
    return node.getPoints()

def play(node:Tabuleiro):
    new_table = list(map(list, node.getGame()))
    new_table = Tabuleiro(new_table)
    while new_table.gameOver() is None:
        new_table = playerPlays(new_table)
        if new_table.gameOver() is not None:
            break
        new_table = min_max_decision(new_table)
        print(new_table)
    print(new_table)
    print(new_table.gameOver())

# def IDFS(initial_board):
#     limit = 0
#     dfslim = False
#     num_nodes_gen = 0
#     while not dfslim:
#         result, dfslim, n_nodes = __DFSLim(initial_board, limit,0)
#         num_nodes_gen += n_nodes
#         if result is not None:
#             return result, num_nodes_gen, limit
#         print("NO SOLUTION FOUND IN LIMIT " + str(limit))
#         limit+=1
#     return None


# from connectFour import getActionsBot, getActionsPlayer
# from tabuleiro import Tabuleiro

# def miniMax(node: Tabuleiro):
#     if node.gameOver()[0] == True:
#         winner = str(node.gameOver()[1]) + " wins!"
#         print(node)
#         return winner



tab = [
    ['-','-','-','-','-','-','-'],
    ['-','-','-','-','-','-','-'],
    ['-','-','-','-','-','-','-'],
    ['-','-','-','-','-','-','-'],
    ['-','-','-','-','-','-','-'],
    ['-','-','-','-','-','-','-']
]

tab = Tabuleiro(tab)
play(tab)

# for i in getActionsBot(tab):
#     print (i, i.getPoints())