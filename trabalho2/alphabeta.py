from tabuleiro import Tabuleiro
from connectFour import getActionsBot, getActionsPlayer, playerPlays

def alpha_beta_decision(board:Tabuleiro) -> Tabuleiro:
    current_value = -10000
    children = getActionsBot(board)
    play = board
    for i in range(len(children)):
        score = minValue(children[i], 1 , 3, -10000, 10000)
        if(score > current_value):
            current_value = score
        if(current_value > 10000):
            alpha = min(current_value, alpha)
            break
        play = children[i]
    return play

def maxValue(node:Tabuleiro, depth:int, limit:int, alpha:int, beta:int):
    if(node.gameOver()):
        return node.getPoints()
    if(depth<limit):
        current_value = -10000
        children = getActionsBot(node)
        for i in range(len(children)):
            score = minValue(children[i], depth+1 , limit, alpha, beta)
            if(score > current_value):
                current_value = score
            if(current_value > beta):
                alpha = min(current_value, alpha)
                break
        return current_value
    return node.getPoints()

def minValue(node:Tabuleiro, depth:int, limit:int, alpha:int, beta:int): 
    if(node.gameOver()):
        return node.getPoints()
    if(depth<limit): 
        current_value = 10000
        children = getActionsPlayer(node)
        for i in range(len(children)):
            score = maxValue(children[i], depth+1 , limit, alpha, beta)
            if(score > current_value):
                current_value = score
            if(current_value < alpha):
                beta = max(current_value, beta)
                break
           
        return current_value
    return node.getPoints()

def play(node:Tabuleiro):
    new_table = list(map(list, node.getGame()))
    new_table = Tabuleiro(new_table)
    while new_table.gameOver() is None:
        new_table = playerPlays(new_table)
        if new_table.gameOver() is not None:
            break
        new_table = alpha_beta_decision(new_table)
        print(new_table)
    print(new_table)
    print(new_table.gameOver())

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
