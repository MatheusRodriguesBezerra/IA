from tabuleiro import Tabuleiro
from connectFour import getActionsBot, getActionsPlayer, playerPlays
from time import time
from random import randrange

def mcts(node: Tabuleiro):
    inicio = time()
    while (inicio + 5) > time():
        leaf = select(node)
        child = expand(leaf)
        result = simulate(child)
        backPropagate(result,child)
    return bestPlay(node)


def select(node: Tabuleiro) -> Tabuleiro:
    new_table = list(map(list, node.getGame()))
    new_table = Tabuleiro(new_table)
    while new_table.gameOver() is None:
        if (new_table.gameOver() is not None) or (getActionsBot(new_table) == []) or (getActionsPlayer(new_table) == []):
            return expand(new_table)
        else:
            new_table = bestUCT(new_table)
    return new_table

def expand(node: Tabuleiro) ->:
    action = chooseAction(node)

def chooseAction(node):
    n = randrange(1,8,1)
    





tab = [
    ['-','-','-','-','-','-','-'],
    ['-','-','-','-','-','-','-'],
    ['-','-','-','-','-','-','-'],
    ['-','-','-','-','-','-','-'],
    ['-','-','-','-','-','-','-'],
    ['-','-','-','-','-','-','-']
]

tab = Tabuleiro(tab)

chooseAction(tab)
