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

def maxValue(node:Tabuleiro, depth:int, limit:int):
    if(node.gameOver()):
        return node.getPoints()
    if(depth<limit): 
        current_value = -10000
        children = getActionsBot(node)
        for i in range(len(children)):
            score = minValue(children[i], depth+1 , limit)
            if(score > current_value):
                current_value = score
        return current_value
    return node.getPoints()

def minValue(node:Tabuleiro, depth:int, limit:int): 
    if(node.gameOver()):
        return node.getPoints()
    
    if(depth<limit): 
        current_value = 10000
        children = getActionsPlayer(node)
        for i in range(len(children)):
            score = maxValue(children[i], depth+1 , limit)
            if(score < current_value):
                current_value = score
        return current_value
    return node.getPoints()

def play(node:Tabuleiro):
    new_table = list(map(list, node.getGame()))
    new_table = Tabuleiro(new_table)
    while new_table.gameTied() is not True:
        new_table = playerPlays(new_table)
        end = new_table.gameOver() 
        if end is not None:
            print(new_table)
            print(end + " WINS")
            break
        print(new_table)

        new_table = min_max_decision(new_table)
        end = new_table.gameOver() 
        if end is not None:
            print(new_table)
            print(end + " WINS")
            break
        print(new_table)

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
