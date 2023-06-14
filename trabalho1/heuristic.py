from Tabuleiro import Tabuleiro

# somatório do número de peças fora do lugar
def Heuristica1(nodeInicial: Tabuleiro, nodeFinal:Tabuleiro) -> int:         
    listInicial = nodeInicial.listOf()
    listFinal = nodeFinal.listOf()
    count = 0
    for i in range(0,16):
        if listFinal[i] != listInicial[i]:
            count += 1
    return count

# manhattan distance
def Heuristica2(nodeInicial: Tabuleiro, nodeFinal:Tabuleiro) -> int:          
    count = 0
    for i in range(0,16):
        xI, yI = nodeInicial.coordinateOf(i)
        xF, yF = nodeFinal.coordinateOf(i)
        diff = abs(xI - xF) + abs(yI - yF)
        count += diff
    return count

