from tabuleiro import Tabuleiro

def botPlays(node: Tabuleiro, n: int):
    new_table = list(map(list, node.getGame()))
    n = n - 1
    for i in range(len(node.getGame())):
        if (new_table[i][n] is not None):
            i = i - 1
            break
    new_table[i][n] = 'X'
    new_table = Tabuleiro(new_table)
    return new_table

def playerPlays(node: Tabuleiro, n: int):
    new_table = list(map(list, node.getGame()))
    n = n - 1
    for i in range(len(node.getGame())):
        if (new_table[i][n] !='-'):
            i = i - 1
            break
    new_table[i][n] = 'O'
    new_table = Tabuleiro(new_table)
    return new_table

def playerPlays2(node: Tabuleiro, n: int):
    new_table = list(map(list, node.getGame()))
    n = n - 1
    for i in range(len(node.getGame())):
        if (new_table[i][n] !='-'):
            i = i - 1
            break
    new_table[i][n] = 'X'
    new_table = Tabuleiro(new_table)
    return new_table

def getActionsBot(node: Tabuleiro):
    actions = []
    for i in range(1,8,1):
        actions.append(botPlays(node,i))
    return actions

def pointsOfList(x:list) -> int:
    if (x.count('O') == 3) and (x.count('X') == 0):
        return -50
    elif (x.count('O') == 2) and (x.count('X') == 0):
        return -10
    elif (x.count('O') == 1) and (x.count('X') == 0):
        return -1
    elif (x.count('O') > 0) and (x.count('X') > 0):
        return 0
    elif (x.count('O') == 0) and (x.count('X') == 0):
        return 0
    elif (x.count('O') == 0) and (x.count('X') == 1):
        return 1
    elif (x.count('O') == 0) and (x.count('X') == 2):
        return 10
    elif (x.count('O') == 0) and (x.count('X') == 3):
        return 50
    else:
        return 0
    
def getPoints(node: Tabuleiro) -> int:
    #PRINT
    m = node.getGame()
    count = 0
    for i in range(0,6,1):     # sequência nas horizontais
        for j in range(0,4,1):
            l = [m[i][j],m[i][j+1],m[i][j+2],m[i][j+3]]
            count = count + pointsOfList(l)

    for i in range(0,3,1):     # sequência nas verticais
        for j in range(0,7,1):
            l = [m[i][j],m[i+1][j],m[i+2][j],m[i+3][j]]
            count = count + pointsOfList(l)

    for i in range(0,3,1):     # sequência nas diagonais positivas
        for j in range(0,4,1):
            l = [m[i][j],m[i+1][j+1],m[i+2][j+2],m[i+3][j+3]]  
            count = count + pointsOfList(l)

    for i in range(3,6,1):     # sequência nas diagonais negativas
        for j in range(0,4,1):
            l = [m[i][j],m[i-1][j+1],m[i-2][j+2],m[i-3][j+3]]
            count = count + pointsOfList(l)

    
    return count



# tab = [[None,None,None,None,None,None,None],
#        [None,None,None,None,None,None,None],
#        ['X', None,None, 'X',None, 'O',None],
#        ['O', None, 'X', 'O',None, 'X', 'X'],
#        ['X', None, 'X', 'O', 'O', 'X', 'X'],
#        [None, None, 'X', None, 'X', 'X', 'X']]

tab = [['-','-','-','-','-','-','-'],
       ['-','-','-','-','-','-','-'],
       ['-', '-','-', '-','-', '-','-'],
       ['-', '-', '-', '-','-', '-', '-'],
       ['-', '-', '-', '-', '-', '-', '-'],
       ['-', '-', '-', '-', '-', '-', '-']]

tab = Tabuleiro(tab)
# print(tab.showGame())
# print(getPoints(tab))
# # botPlays(tab, 2)
# c = getActionsBot(tab)
# for item in c:
#     print(item)
#     print(getPoints(item))
while(True):
    print(tab) 
    play = int(input("Which column u want to put:\n1-7\n"))
    tab = playerPlays(tab, play)
    print(tab)

    play = int(input("Which column u want to put:\n1-7\n"))
    tab = playerPlays2(tab, play)