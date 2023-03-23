from connectFour import getActionsBot, getActionsPlayer
from tabuleiro import Tabuleiro

def miniMax(node: Tabuleiro):
    if node.gameOver()[0] == True:
        winner = str(node.gameOver()[1]) + " wins!"
        print(node)
        return winner
    



def MIN(node:Tabuleiro): 
    childs = []
    childsPoints = []

    for child in getActionsPlayer(node):
        childs.append(child)
        childsPoints.append(child.getPoints())

    tmp = max(childsPoints)
    minIndex = childsPoints.index(tmp)

    return childs[minIndex]

def MAX(node:Tabuleiro): 
    childs = []
    childsPoints = []

    for child in getActionsBot(node):
        childs.append(child)
        childsPoints.append(child.getPoints())

    tmp = min(childsPoints)
    minIndex = childsPoints.index(tmp)

    return childs[minIndex]

tab = [
    ['-','-','-','-','-','-','-'],
    ['-','-','-','-','-','-','-'],
    ['-','-','-','-','O','-','-'],
    ['-','-','-','-','O','-','-'],
    ['-','-','-','-','O','-','-'],
    ['X','X','-','X','O','-','-']
]

tab = Tabuleiro(tab)
print(miniMax(tab))