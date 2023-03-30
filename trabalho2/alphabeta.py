from tabuleiro import Tabuleiro
from connectFour import getActionsBot, getActionsPlayer, playerPlays
import time

def alpha_beta_decision(board:Tabuleiro) -> Tabuleiro:
    start_time = time.time()
    current_value = -10000
    children = getActionsBot(board) 
    decision_index = 0
    num_nodes = 0
    for i in (range(len(children))):
        if(children[i].getPoints() == 512):
            return children[i]
        call = minValue(children[i], 1, 5, -10000, 10000, 1)
        score = max(current_value, call[0])
        num_nodes+= call[1]
        if(score > current_value):
            current_value = score
            decision_index = i
            play = children[i]
    end_time = time.time()
    print("----------- BOT: "+ str(decision_index + 1) + " -----------")
    print("\nTEMPO DE RESPOSTA: ", end_time - start_time)
    print("NUMERO DE NÓS CRIADOS: ",num_nodes)
    return play

def maxValue(node:Tabuleiro, depth:int, limit:int, alpha:int, beta:int, num_nodes):
    if(node.gameOver()):
        return node.getPoints(), num_nodes
    if(depth == limit):
        return node.getPoints(), num_nodes
    score = -10000
    for child in getActionsBot(node):
        call = minValue(child, depth+1 , limit, alpha, beta, 1)
        score = max(score, call[0])
        num_nodes+= call[1]
        if score >= beta:
            return score, num_nodes
        alpha = max(alpha, score)
    return score, num_nodes

def minValue(node:Tabuleiro, depth:int, limit:int, alpha:int, beta:int, num_nodes): 
    if(node.gameOver()):
        return node.getPoints(), num_nodes
    if(depth == limit):
        return node.getPoints(), num_nodes
    score = 10000
    for child in getActionsPlayer(node):
        call = maxValue(child, depth+1 , limit, alpha, beta, 1)
        score = min(score, call[0])
        num_nodes+= call[1]
        if score <= alpha:
            return score, num_nodes
        beta = min(beta, score)
    return score, num_nodes

def play_alpha_beta(node:Tabuleiro):
    new_table = node
    while new_table.gameTied() is not True:
        new_table = playerPlays(new_table)
        end = new_table.gameOver() 
        if end is not None:
            print(new_table)
            print(end + " WINS")
            return
        print(new_table)
        new_table = alpha_beta_decision(new_table)
        end = new_table.gameOver() 
        if end is not None:
            print(new_table)
            print(end + " WINS")
            return
        print(new_table)
    print("------------ EMPATE ------------")
