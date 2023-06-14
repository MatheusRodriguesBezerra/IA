from Tabuleiro import Tabuleiro
from heuristic import Heuristica1, Heuristica2
from basics import getActions

def Gulosa(node: Tabuleiro, configFinal: Tabuleiro):
    visited = []
    abertos = []
    path = [node.getGame()]
    i = 0
    while node.getGame() != configFinal.getGame():
        visited.append(node.getGame())
        for child in getActions(node):
            if child.getGame() not in visited:
                abertos.append((child.getGame(), Heuristica1(child)))
        abertos.sort(key=lambda tup: tup[1])
        best = abertos[0]
        node = best[0]
        abertos = []
        node = Tabuleiro(node)
        path.append(node.getGame())
        i = i + 1
    return node.getGame(), len(visited), i 
