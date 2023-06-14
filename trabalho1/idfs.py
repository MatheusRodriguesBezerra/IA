from Tabuleiro import Tabuleiro, getActions, thereIsSolution


def LDFS(node: Tabuleiro, nodeFinal: Tabuleiro, limit:int):
    q = [node]  
    visited = [q]
    while q != []:
        u = q[-1]
        q.pop()
        for w in getActions(u):
            if u.depth < limit:
                if w == nodeFinal:
                    path = [] 
                    while w != None:
                        path.append(w)
                        print(w)
                        w = w.parent
                    return path
                if w != None:
                    w.parent = u
                    w.depth = u.depth+1
                    visited.append(w)
                    q.append(w)       
    return None

def IDFS(nodeInicial: Tabuleiro, nodeFinal: Tabuleiro):
    if thereIsSolution(nodeInicial, nodeFinal) == False:
        return -1
    limit = 1
    result = None
    while result == None:
        result = LDFS(nodeInicial, nodeFinal, limit)
        print(limit)
        limit = limit + 1
    return result



tab1 = Tabuleiro([[1, 2, 3, 4], [5, 6, 8, 12], [13, 9, 0, 7], [14, 11, 10, 15]])
tab2 = Tabuleiro([[1, 2, 3, 4], [13, 6, 8, 12], [5, 9, 0, 7], [14, 11, 10, 15]])
tab3 = Tabuleiro([[1, 2, 3, 4], 
                  [5, 6, 7, 0], 
                  [9, 10, 11, 8], 
                  [13, 14, 15, 12]])
tabFinal = Tabuleiro([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]])


print(IDFS(tab1,tabFinal))
