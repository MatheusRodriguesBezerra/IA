import sys
sys.setrecursionlimit(10**6)
import time 

class Tabuleiro:
    def __init__(self, game, parent=None):
        self.game = game
        self.parent = parent

    def __eq__(self, other):
        if other == None:
            return False
        else:
            m1 = self.getGame()
            m2 = other.getGame()
            return m1 == m2

    def getParent(self):
        return self.parent

    def showGame(self):
        m = self.getGame()
        resultado = ""
        i,j = 0,0
        while i < 4:
            resultado = resultado + str(m[i][0]) + " " + str(m[i][1]) + " " + str(m[i][2]) + " " + str(m[i][3]) + "\n"
            i = i + 1
        return resultado

    def getGame(self):
        nTabuleiro = Tabuleiro(self.game)
        return nTabuleiro.game

    def getBlankRow(self):
        matriz = self.getGame()
        i,j = 0,0
        while i < 4:
            while j < 4:
                if matriz[i][j] == 0:
                    return j
                j = j + 1
            j = 0
            i = i + 1
    
    def getBlankLine(self):
        matriz = self.getGame()
        i,j = 0,0
        while i < 4:
            while j < 4:
                if matriz[i][j] == 0:
                    return i
                j = j + 1
            j = 0
            i = i + 1
    
    def listofMatrix(self):
        i, j = 0,0
        lista = []
        matriz = self.getGame()
        while i < 4:
            while j < 4:
                lista.append(matriz[i][j])
                j = j + 1
            j = 0
            i = i + 1
        return lista    
    
    def numberofInversions(self):
        count, i = 0, 0
        j = 1
        lista = list(self.listofMatrix())
        while i < 16:
            while j < 16:
                if lista[i] > lista[j] and lista[i] != 0 and lista[j] != 0:
                    count = count + 1
                j = j + 1
            i = i + 1
            j = i + 1
        return count
    
    def indexOf(self,value: int):
        matriz = self.getGame()
        i,j = 0,0
        while i < 4:
            while j < 4:
                if matriz[i][j] == value:
                    return i,j
                j = j + 1
            i = i + 1
            j = 0


def thereIsSolution(x: Tabuleiro, y: Tabuleiro):
    condI = (x.numberofInversions() % 2 == 0) == ((x.getBlankLine()+1) % 2 == 1)
    condF = (y.numberofInversions() % 2 == 0) == ((y.getBlankLine()+1) % 2 == 1)
    return condI == condF

def moveLeft(x: Tabuleiro):
    new_table = list(map(list, x.getGame()))
    new_table = Tabuleiro(new_table)
    if new_table.getBlankRow()-1 < 0:
        return None
    else:
        nullRow = new_table.getBlankRow()
        nullLine = new_table.getBlankLine()
        novox = new_table.getGame()
        novox[nullLine][nullRow] = novox[nullLine][nullRow-1]
        novox[nullLine][nullRow-1] = 0
        novox = Tabuleiro(novox)
        return novox
    
def moveDown(x: Tabuleiro):
    new_table = list(map(list, x.getGame()))
    new_table = Tabuleiro(new_table)
    if new_table.getBlankLine()+1 > 3:
        return None
    else:
        nullRow = new_table.getBlankRow()
        nullLine = new_table.getBlankLine()
        novox = new_table.getGame()
        novox[nullLine][nullRow] = novox[nullLine+1][nullRow]
        novox[nullLine+1][nullRow] = 0
        novox = Tabuleiro(novox)
        return novox
        
def moveRight(x: Tabuleiro):
    new_table = list(map(list, x.getGame()))
    new_table = Tabuleiro(new_table)
    if new_table.getBlankRow()+1 > 3:
        return None
    else:
        nullRow = new_table.getBlankRow()
        nullLine = new_table.getBlankLine()
        novox = new_table.getGame()
        novox[nullLine][nullRow] = novox[nullLine][nullRow+1]
        novox[nullLine][nullRow+1] = 0
        novox = Tabuleiro(novox)
        return novox

def moveUp(x: Tabuleiro):
    new_table = list(map(list, x.getGame()))
    new_table = Tabuleiro(new_table)
    if new_table.getBlankLine()-1 < 0:
        return None
    else:
        nullRow = new_table.getBlankRow()
        nullLine = new_table.getBlankLine()
        novox = new_table.getGame()
        novox[nullLine][nullRow] = novox[nullLine-1][nullRow]
        novox[nullLine-1][nullRow] = 0
        novox = Tabuleiro(novox)
        return novox

def getActions(x: Tabuleiro):
    actions = []
    if moveRight(x) is not None:
        actions.append(moveRight(x))
    if moveDown(x) is not None:
        actions.append(moveDown(x))
    if moveLeft(x) is not None:
        actions.append(moveLeft(x))
    if moveUp(x) is not None:
        actions.append(moveUp(x))
    return actions

def DFS(node: Tabuleiro, configFinal: Tabuleiro) -> Tabuleiro|list:
    visited = []
    DfsRec(node, configFinal, visited)

def DfsRec(node: Tabuleiro, configFinal: Tabuleiro, visited: list):
    if node.getGame() == configFinal.getGame():
        return node.getGame(), len(visited)
    visited.append(node.getGame())
    for child in getActions(node):
        DfsRec(child, configFinal, visited) 


def DFSInit(configInicial: Tabuleiro, configFinal: Tabuleiro):
    if thereIsSolution(configInicial,configFinal) == True:
        return DFS(configInicial, configFinal)
    else:
        return None

def BFS(node: Tabuleiro, configFinal: Tabuleiro) -> Tabuleiro|str:
    visited = [node.getGame()] # lista dos nós já visitados
    queue = [node.getGame()] # pilha
    while len(queue) > 0:
        v = queue[0]
        v = Tabuleiro(v)
        for child in getActions(v):
            if not child.getGame() in visited:
                queue.append(child.getGame())
                visited.append(child.getGame())
                if child == configFinal:
                    return child.getGame(), len(visited)      
        queue.pop(0)
    return None, None

def BFSInit(configInicial: Tabuleiro, configFinal: Tabuleiro):
    if thereIsSolution(configInicial,configFinal) == True:
        return BFS(configInicial, configFinal)
    else:
        return "sem solução"

def LDFS(node: Tabuleiro, configFinal: Tabuleiro, limit:int ,visited:list):
    visited.append(node.getGame())
    if node == configFinal:
        return visited  
    children = getActions(node)  
    if limit == 0:
        return []
    for child in children:
        if not child.getGame() in visited:
            path = LDFS(child,configFinal,limit-1,list(map(list,visited)))
            if configFinal.getGame() in path:
                return path
    return []

def IDFS(configInicial: Tabuleiro, configFinal: Tabuleiro):
    visited = []
    limit = 1
    path = []
    while configFinal.getGame() not in path:
        path = LDFS(configInicial, configFinal, limit, visited)
        limit = limit + 1
    return configFinal.getGame(), limit-1, 3**(limit-1)

def Heuristica1(node: Tabuleiro) -> int:      #somatório do número de peças fora do lugar   
    configFinal = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]]
    configFinal = Tabuleiro(configFinal)
    configFinal = configFinal.listofMatrix()
    node = node.listofMatrix()
    i,count = 0, 0
    while i < 16:
        if configFinal[i] != node[i]:
            count = count + 1
        i = i + 1
    return count

def Heuristica2(node: Tabuleiro) -> int:       # manhattan distance     
    configFinal = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]]
    configFinal = Tabuleiro(configFinal)
    i, count = 0, 0
    while i < 16:
        xI, yI = node.indexOf(i)
        xF, yF = configFinal.indexOf(i)
        diff = abs(xI - xF) + abs(yI - yF)
        count = count + diff
        i = i + 1
    return count

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

def strToTabuleiro(msg: str) -> Tabuleiro:
    msg = msg.split()
    lista = []
    for i in msg:
        lista.append(int(i))
    matriz = []
    for i in range(4):
        matriz.append([0] * 4)
    k = 0
    for i in range(4):
        for j in range(4):
            matriz[i][j] = lista[k]
            k += 1
    matriz = Tabuleiro(matriz)
    return matriz.getGame()

def main():
    configInicial = str(input("Configuracao inicial: "))
    configFinal = str(input("Configuracao Final: "))
    typeOfSearch = int(input("Qual tipo de busca que pretendes?"))
    configInicial = strToTabuleiro(configInicial)
    configFinal = strToTabuleiro(configFinal)
    if typeOfSearch == 1:
        inicio = time.time()
        resposta, memory = DFSInit(configInicial, configFinal)
        fim = time.time()
        print("-------------------- DFS -----------------------")
        print(resposta)
        print(memory)
        print("Tempo gasto: " + fim - inicio + " segundos")
        return 0
    elif typeOfSearch == 2:
        inicio = time.time()
        resposta, espaco = BFSInit(Tabuleiro(configInicial), Tabuleiro(configFinal))
        fim = time.time()
        tempo = fim - inicio
        print("-------------------- BFS -----------------------")
        print(resposta)
        print("foram criados %d espaços de memória" % (espaco))
        print("Tempo gasto: %.6f segundos" % (tempo))
        return 0
    elif typeOfSearch == 3:
        inicio = time.time()
        resposta, espaco,depth = IDFS(Tabuleiro(configInicial), Tabuleiro(configFinal))
        fim = time.time()
        tempo = fim - inicio
        print("-------------------- IDFS -----------------------")
        print(resposta)
        print("Espaço aproximado criado: %d " % (depth))
        print("Profundidade: %d" % (espaco))
        print("Tempo gasto: %.6f segundos" % (tempo))
        return 0
    elif typeOfSearch == 4:
        inicio = time.time()
        resposta, espaco, depth = Gulosa(Tabuleiro(configInicial), Tabuleiro(configFinal))
        fim = time.time()
        tempo = fim - inicio
        print("-------------------- GULOSO -----------------------")
        print(resposta)
        print("Espaço aproximado criado: %d " % (depth))
        print("Profundidade: %d" % (espaco))
        print("Tempo gasto: %.6f segundos" % (tempo))
        return 0
    elif typeOfSearch == 5:
        inicio = time.time()
        resposta, espaco, depth = AstarInit(Tabuleiro(configInicial), Tabuleiro(configFinal))
        fim = time.time()
        tempo = fim - inicio
        print("-------------------- Aestrela -----------------------")
        print(resposta)
        print("Espaço aproximado criado: %d " % (depth))
        print("Profundidade: %d" % (espaco))
        print("Tempo gasto: %.6f segundos" % (tempo))
        return 0
    
main()

