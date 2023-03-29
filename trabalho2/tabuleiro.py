class Tabuleiro:
    def __init__(self, game, parent=None):
        self.game = game
        self.points = self.setBoardPoints()
        self.colsDone = self.columnsFinished()
        # novos atributos
        self.visits = 0     # contador de quantas vezes este tabaleiro ja foi visitado
        self.childs = [] # lista dos filhos ja criados
        self.reward = 0.0 # pontuação deste nó
        self.parent = parent # pai

    def getGame(self):
        return self.game

    def getPoints(self):
        return self.points

    def getColumnsDone(self):
        return self.colsDone

    def __str__(self):
        string = ""
        for i in self.game:
            string += str(i) + '\n'
        return string
    
    def __eq__(self, other):
        if(type(other) is not Tabuleiro):
            return False
        return self.game == other.game

    def __pointsOfList(self, x:list) -> int:
        num_O = x.count('O')
        num_X = x.count('X')

        if(num_X == 4):
            return - 512
        elif(num_O == 4):
            return 512
        
        if(num_X == 0):
            if(num_O == 3):
                return 50
            elif(num_O == 2):
                return 10
            elif(num_O == 1):
                return 1
            else:
                return 0
        elif(num_O == 0):
            if(num_X == 3):
                return -50
            elif(num_X == 2):
                return -10
            elif(num_X == 1):
                return -1
            else:
                return 0
        else:
            return 0
    
    def setBoardPoints(self) -> int:
        board = self.game
        count = 0
        for i in range(0,6,1):     # sequência nas horizontais
            for j in range(0,4,1):
                sequence_of_four_horizontal = [board[i][j],board[i][j+1],board[i][j+2],board[i][j+3]]
                points = self.__pointsOfList(sequence_of_four_horizontal)
                if(abs(points)==512):
                    return points
                count = count + points

        for i in range(0,3,1):     # sequência nas verticais
            for j in range(0,7,1):
                sequence_of_four_vertical = [board[i][j],board[i+1][j],board[i+2][j],board[i+3][j]]
                points = self.__pointsOfList(sequence_of_four_vertical)
                if(abs(points)==512):
                    return points
                count = count + points
                
        for i in range(0,3,1):     # sequência nas diagonais positivas
            for j in range(0,4,1):
                sequence_of_four_diagonal_1 = [board[i][j],board[i+1][j+1],board[i+2][j+2],board[i+3][j+3]]  
                points = self.__pointsOfList(sequence_of_four_diagonal_1)
                if(abs(points)==512):
                    return points
                count = count + points

        for i in range(3,6,1):     # sequência nas diagonais negativas
            for j in range(0,4,1):
                sequence_of_four_diagonal_2 = [board[i][j],board[i-1][j+1],board[i-2][j+2],board[i-3][j+3]]
                points = self.__pointsOfList(sequence_of_four_diagonal_2)
                if(abs(points)==512):
                    return points
                count = count + points
        return count

    def columnsFinished(self):
        colsDone = [False, False, False, False, False, False, False]
        for i in range(len(self.game[0])):
            col = [row[i] for row in self.game]
            if(col.count('-') == 0):
                colsDone[i] = True
        return colsDone

    def gameOver(self):
        if(self.points >= 512):
            return 'BOT'
        elif(self.points <= -512):
            return 'PLAYER'
        else:
            None

    def gameTied(self):
        if self.colsDone.count(True) == 7:
            return True
        return False

    # novas funções
    def gameFinished(self): # retorna se o jogo acabou 
        if (self.gameOver() is not None) or (self.gameTied() == True):
            return True
        else:
            return False 

    def update(self, result):
        self.visits += 1
        self.wins += result