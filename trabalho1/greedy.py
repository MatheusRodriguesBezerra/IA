from Tabuleiro import Tabuleiro, getActions, thereIsSolution
from heuristic import Heuristica1, Heuristica2


def Greedy(node: Tabuleiro, configFinal: Tabuleiro):
    visited = []
    q = [(Heuristica2(node, configFinal), node)]
    while q != []:
        hu, u = q[0]
        if u == configFinal:
            return u
        visited.append((hu, u))
        for w in getActions(u):
            w.parent = u
            w.depth = u.depth+1
            q.append((Heuristica2(w, configFinal), w))
        q.sort(key=lambda tup: tup[0])

tab1 = Tabuleiro([[1, 2, 3, 4], [5, 6, 8, 12], [13, 9, 0, 7], [14, 11, 10, 15]])
tab2 = Tabuleiro([[1, 2, 3, 4], [13, 6, 8, 12], [5, 9, 0, 7], [14, 11, 10, 15]])
tab3 = Tabuleiro([[1, 2, 3, 4], 
                  [5, 6, 7, 0], 
                  [9, 10, 11, 8], 
                  [13, 14, 15, 12]])
tabFinal = Tabuleiro([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]])


print(Greedy(tab1, tabFinal))