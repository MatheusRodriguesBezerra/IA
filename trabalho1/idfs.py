from Tabuleiro import Tabuleiro, getActions, thereIsSolution


def LDFS(node: Tabuleiro, nodeFinal: Tabuleiro, limit:int):
    q = [node]  
    visited = [node]
    path = []
    while q != []:
        u = q[-1]
        q.pop()
        for w in getActions(u):
            if u.depth < limit:
                w.parent = u
                w.depth = u.depth+1
                visited.append(w)
                q.append(w)       
                if w == nodeFinal: 
                    while w != None:
                        path.append(w)
                        w = w.parent
                    return path
    return None
    

def IDFS(nodeInicial: Tabuleiro, nodeFinal: Tabuleiro):
    if thereIsSolution(nodeInicial, nodeFinal) == False:
        return -1
    limit = 1
    result = None
    while result == None:
        result = LDFS(nodeInicial, nodeFinal, limit)
        limit = limit + 1
    return result



