from tabuleiro import Tabuleiro
from connectFour import getActionsBot, makeMove
from time import time
from math import sqrt, log
from random import randrange

# Realiza a busca com Monte Carlo Tree Search (MCTS).
def mcts(node: Tabuleiro) -> Tabuleiro:
    inicio = time()
    while (inicio + 5) > time():    # limite de 5 segundos
        leaf = select(node)
        child = expand(leaf)
        result = simulate(child)
        backPropagate(child, result)
    return bestPlay(node)

# tem que alcançar um nó-folha
def select(node: Tabuleiro) -> Tabuleiro:
    node.visits += 1
    while getActionsBot(node): #ainda tem que resolver como fazer para alternar a vez do 'O' ou do 'X'
        node = bestUCT(node)
    return node

# retorna o descendente mais promissor a partir do UCT 
def bestUCT(node: Tabuleiro) -> Tabuleiro:
    best_score = -10000
    best_child = None
    for i in getActionsBot(node): #ainda tem que resolver como fazer para alternar a vez do 'O' ou do 'X'
        exploit_score = AvarageWin(i)
        print(i.visits +1)
        print(2*log(node.visits+2))
        explore_score = sqrt((2*(log(2))) / 2)
        print(explore_score)
        score = exploit_score + explore_score
        if score > best_score:
            best_score = score
            best_child = i
    return best_child

# retorna a média de pontuação dos filhos  
def AvarageWin(node: Tabuleiro) -> float:
    new_table = list(map(list, node.getGame()))
    new_table = Tabuleiro(new_table)
    soma = 0 # soma das pontuações do filho
    n = 0 # soma da quantidade de filhos
    for i in getActionsBot(node):
        soma += i.getPoints()
        n += 1
    resultado = soma / n
    return resultado

# Expande o nó selecionado pela função select(), adicionando um novo filho não explorado.
def expand(node: Tabuleiro) -> Tabuleiro:
    n = chooseAction()
    new_node = makeMove(node, n, 'PLAYER') #ainda tem que resolver como fazer para alternar a vez do 'O' ou do 'X'
    new_node = Tabuleiro(new_node, parent=node)
    node.childs.append(new_node)
    return new_node

# retorna um número aleaório entre 1-8
def chooseAction():
    n = randrange(1,8)
    return n

# Realiza a simulação de Monte Carlo a partir do nó selecionado pela função seleção(), 
# escolhendo ações aleatórias até chegar a um estado final.
def simulate(node: Tabuleiro) -> int:
    new_table = list(map(list, node.getGame()))
    new_table = Tabuleiro(new_table)
    while new_table.gameFinished() == False:
        n = chooseAction()
        new_table = makeMove(new_table, n, jogadorDaVez) #ainda tem que resolver como fazer para alternar a vez do 'O' ou do 'X'        
        if jogadorDaVez == 'PLAYER':
            jogadorDaVez = 'BOT'
        else:
            jogadorDaVez = 'PLAYER'
    return new_table.getPoints()

# Atualiza as estatísticas dos nós visitados a partir do nó selecionado pela função seleção() até a raiz.
def backPropagate(node:Tabuleiro, result: int):
    while node.parent is not None:
        node.visits += 1
        node.reward += result
        node = node.parent

# Retorna o melhor filho do nó atual, usando a política de seleção UCB.
def bestPlay(node: Tabuleiro):
    best_value = -1000000
    for i in node.childs:
        value = i.reward / i.visits
        if value > best_value:
            best_value = value
            best_son = i
    return best_son


tab = [
    ['-','-','-','-','-','-','-'],
    ['-','-','-','-','-','-','-'],
    ['-','-','-','-','-','-','-'],
    ['-','-','-','-','-','-','-'],
    ['-','-','-','-','-','-','-'],
    ['-','-','-','X','-','-','-']
]

tab = Tabuleiro(tab)

print(bestUCT(tab))



