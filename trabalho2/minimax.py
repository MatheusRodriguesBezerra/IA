from tabuleiro import Tabuleiro
from connectFour import getActionsBot, getActionsPlayer,playerPlays

def min_max_decision(board:Tabuleiro) -> Tabuleiro:
    current_value = -10000
    children = getActionsBot(board)
    play = board
    for i in range(len(children)):
        if(children[i].getPoints() == 512):
            return children[i]
        score = max(current_value, minValue(children[i], 1 , 6))
        # print(score)
        if(score > current_value):
            current_value = score
            play = children[i]
    print("FINAL CHOSEN: ",current_value)
    return play

def maxValue(node:Tabuleiro, depth:int, limit:int):
    if(node.gameOver()):
        return node.getPoints()
    if(depth == limit):
        return node.getPoints()
    score = -10000
    children = getActionsBot(node)
    for child in children:
        score = max(score,minValue(child, depth+1 , limit))
    return score

def minValue(node:Tabuleiro, depth:int, limit:int): 
    if(node.gameOver()):
        return node.getPoints()
    if(depth == limit):
        return node.getPoints()
    score = 10000
    children = getActionsPlayer(node)
    for child in children:
        score = min(score,maxValue(child, depth+1 , limit))
    return score

def play_min_max(tab):
    new_table = Tabuleiro(tab)
    while new_table.gameTied() is not True:
        new_table = playerPlays(new_table)
        end = new_table.gameOver() 
        if end is not None:
            print(new_table)
            print(end + " WINS")
            break

        new_table = min_max_decision(new_table)
        end = new_table.gameOver() 
        if end is not None:
            print(new_table)
            print(end + " WINS")
            break
        print(new_table)

