import sys
sys.setrecursionlimit(10**6)
import time 
from Tabuleiro import Tabuleiro

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

