from Tabuleiro import Tabuleiro, getActions, thereIsSolution

def DFS(nodeInicial: Tabuleiro, nodeFinal: Tabuleiro):
    if thereIsSolution(nodeInicial, nodeFinal) == False:
        return -1
    q = []
    visited = [nodeInicial.game]
    q.append(nodeInicial)
    nodeInicial.visited = True
    while q != []:
        u = q[-1]
        print(u)
        q.pop()
        for w in getActions(u):
            if w == nodeFinal:
                break
            if (w != None) and (w.game not in visited):
                w.parent = u
                q.append(w)
                visited.append(w.game)

    while True:
        print(w)
        if w.parent == None:
            break
        w = w.parent



tab1 = Tabuleiro([[1, 2, 3, 4], [5, 6, 8, 12], [13, 9, 0, 7], [14, 11, 10, 15]])
tab2 = Tabuleiro([[1, 2, 3, 4], [13, 6, 8, 12], [5, 9, 0, 7], [14, 11, 10, 15]])
tab3 = Tabuleiro([[1, 2, 3, 4], 
                  [5, 6, 7, 0], 
                  [9, 10, 11, 8], 
                  [13, 14, 15, 12]])
tabFinal = Tabuleiro([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]])


print(DFS(tab1,tabFinal))