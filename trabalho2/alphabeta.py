from tabuleiro import Tabuleiro
from connectFour import getActionsBot, getActionsPlayer, playerPlays

def alpha_beta_decision(board:Tabuleiro) -> Tabuleiro:
    current_value = -10000
    children = getActionsBot(board) 
    decision_index = 0
    for i in (range(len(children))):
        if(children[i].getPoints() == 512):
            return children[i]
        score = max(current_value, minValue(children[i], 1 , 6, -10000, 10000))
        if(score > current_value):
            current_value = score
            decision_index = i
            play = children[i]
    print("----------- BOT: "+ str(decision_index + 1) + " -----------")
    return play

def maxValue(node:Tabuleiro, depth:int, limit:int, alpha:int, beta:int):
    if(node.gameOver()):
        return node.getPoints()
    if(depth == limit):
        return node.getPoints()
    score = -10000
    for i in getActionsBot(node):
        score = max(score, minValue(i, depth+1 , limit, alpha, beta))
        if score >= beta:
            return score
        alpha = max(alpha, score)
    return score

def minValue(node:Tabuleiro, depth:int, limit:int, alpha:int, beta:int): 
    if(node.gameOver()):
        return node.getPoints()
    if(depth == limit):
        return node.getPoints()
    score = 10000
    for i in getActionsPlayer(node):
        score = min(score, maxValue(i, depth+1 , limit, alpha, beta))
        if score <= alpha:
            return score
        beta = min(beta, score)
    return score

def play_alpha_beta(node:Tabuleiro):
    new_table = Tabuleiro(node)
    while new_table.gameTied() is not True:
        new_table = playerPlays(new_table)
        end = new_table.gameOver() 
        if end is not None:
            print(new_table)
            print(end + " WINS")
            break
        print(new_table)
        new_table = alpha_beta_decision(new_table)
        end = new_table.gameOver() 
        if end is not None:
            print(new_table)
            print(end + " WINS")
            break
        print(new_table)
    print("------------ EMPATE ------------")
