from Tabuleiro import Tabuleiro
from heuristic import Heuristica1, Heuristica2
from basics import getActions, thereIsSolution

def Astar(node: Tabuleiro, configFinal: Tabuleiro):
    abertos = [(node.getGame(),Heuristica2(node))]
    visited = []
    i = 0
    while abertos:
        i = i + 1
        abertos.sort(key=lambda tup: tup[1])
        new = abertos[0]
        new = Tabuleiro(new[0])
        if new == configFinal:
            return new.getGame(), len(visited), i
        else:
            visited.append(abertos[0])
            abertos.pop(0)
        for child in getActions(new):
            if not (child.getGame(),Heuristica2(child)) in visited:
                abertos.append((child.getGame(),Heuristica2(child)))
    return None, None, None

def AstarInit(node: Tabuleiro, configFinal: Tabuleiro):
    if thereIsSolution(node, configFinal):
        return Astar(node, configFinal)
    else:
        return None, None, None
