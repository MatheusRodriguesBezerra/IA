class Tabuleiro:
    def __init__(self, game:list, parent=None, depth=0):
        self.game = game
        self.parent = parent
        self.depth = depth
        self.visited = False

    def __eq__(self, other):
        if other == None:
            return False
        else:
            m1 = self.game
            m2 = other.game
            return m1 == m2

    def __str__(self):
        m = self.game
        resultado = ""
        i = 0
        while i < 4:
            resultado = resultado + str(m[i][0]) + "\t" + str(m[i][1]) + "\t" + str(m[i][2]) + "\t" + str(m[i][3]) + "\n"
            i = i + 1
        return resultado

    def blankColumn(self) -> int:
        matriz = self.game
        for i in range(0,4):
            for j in range(0,4):
                if matriz[i][j] == 0:
                    return j
    
    def blankLine(self) -> int:
        matriz = self.game
        for i in range(0,4):
            for j in range(0,4):
                if matriz[i][j] == 0:
                    return i
    
    def listOf(self) -> list:
        lista = []
        matriz = self.game
        for i in range(0,4):
            for j in range(0,4):
                lista.append(matriz[i][j])
        return lista    
    
    def numberofInversions(self):
        count, i = 0, 0
        j = 1
        lista = list(self.listOf())
        while i < 16:
            while j < 16:
                if lista[i] > lista[j] and lista[i] != 0 and lista[j] != 0:
                    count = count + 1
                j = j + 1
            i = i + 1
            j = i + 1
        return count
    
    def coordinateOf(self,value: int):
        matriz = self.game
        for i in range(0,4):
            for j in range(0,4):
                if matriz[i][j] == value:
                    return i,j


def thereIsSolution(x: Tabuleiro, y: Tabuleiro) -> bool:
    condI = (x.numberofInversions() % 2 == 0) == ((x.blankLine()+1) % 2 == 1)
    condF = (y.numberofInversions() % 2 == 0) == ((y.blankLine()+1) % 2 == 1)
    return condI == condF


def moveLeft(x: Tabuleiro) -> Tabuleiro | None:
    new_table = Tabuleiro(list(map(list, x.game)))
    nullLine, nullColumn = new_table.coordinateOf(0)
    if nullColumn == 0:
        return None
    else:
        novox = new_table.game
        novox[nullLine][nullColumn] = novox[nullLine][nullColumn-1]
        novox[nullLine][nullColumn-1] = 0
        novox = Tabuleiro(novox)
        return novox
   
def moveDown(x: Tabuleiro) -> Tabuleiro | None:
    new_table = Tabuleiro(list(map(list, x.game)))
    nullLine, nullColumn = new_table.coordinateOf(0)
    if nullLine == 3:
        return None
    else:
        novox = new_table.game
        novox[nullLine][nullColumn] = novox[nullLine+1][nullColumn]
        novox[nullLine+1][nullColumn] = 0
        novox = Tabuleiro(novox)
        return novox

def moveRight(x: Tabuleiro) -> Tabuleiro | None:
    new_table = Tabuleiro(list(map(list, x.game)))
    nullLine, nullColumn = new_table.coordinateOf(0)
    if nullColumn == 3:
        return None
    else:
        novox = new_table.game
        novox[nullLine][nullColumn] = novox[nullLine][nullColumn+1]
        novox[nullLine][nullColumn+1] = 0
        novox = Tabuleiro(novox)
        return novox

def moveUp(x: Tabuleiro) -> Tabuleiro | None:
    new_table = Tabuleiro(list(map(list, x.game)))
    nullLine, nullColumn = new_table.coordinateOf(0)
    if nullLine == 0:
        return None
    else:
        novox = new_table.game
        novox[nullLine][nullColumn] = novox[nullLine-1][nullColumn]
        novox[nullLine-1][nullColumn] = 0
        novox = Tabuleiro(novox)
        return novox

def getActions(x: Tabuleiro):
    actions = []
    if moveRight(x) != None:
        actions.append(moveRight(x))
    if moveLeft(x) != None:
        actions.append(moveLeft(x))
    if moveDown(x) != None:
        actions.append(moveDown(x))
    if moveUp(x) != None:
        actions.append(moveUp(x))
    return actions
