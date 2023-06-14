from Tabuleiro import Tabuleiro, getActions, thereIsSolution

def BFS(nodeInicial: Tabuleiro, nodeFinal: Tabuleiro):
    if thereIsSolution(nodeInicial, nodeFinal) == False:
        return -1
    q = [nodeInicial]
    visited = [nodeInicial.game]
    while q != []:
        u = q[0]
        if u == nodeFinal:
            break
        q.pop(0)
        for w in getActions(u):
            if (w != None) and (w.game not in visited):
                w.parent = u
                q.append(w)
                visited.append(w.game)

    path = [] 
    while u != None:
        path.append(u)
        print(u)
        u = u.parent
    return path
