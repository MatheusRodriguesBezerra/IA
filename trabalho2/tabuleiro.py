class Tabuleiro:
    def __init__(self, game):
        self.game = game
        self.points = self.setBoardPoints()
        self.colsDone = self.columnsFinished()

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
                count = count + self.__pointsOfList(sequence_of_four_horizontal)

        for i in range(0,3,1):     # sequência nas verticais
            for j in range(0,7,1):
                sequence_of_four_vertical = [board[i][j],board[i+1][j],board[i+2][j],board[i+3][j]]
                count = count + self.__pointsOfList(sequence_of_four_vertical)

        for i in range(0,3,1):     # sequência nas diagonais positivas
            for j in range(0,4,1):
                sequence_of_four_diagonal_1 = [board[i][j],board[i+1][j+1],board[i+2][j+2],board[i+3][j+3]]  
                count = count + self.__pointsOfList(sequence_of_four_diagonal_1)

        for i in range(3,6,1):     # sequência nas diagonais negativas
            for j in range(0,4,1):
                sequence_of_four_diagonal_2 = [board[i][j],board[i-1][j+1],board[i-2][j+2],board[i-3][j+3]]
                count = count + self.__pointsOfList(sequence_of_four_diagonal_2)
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
            return 'PLAYER'
        elif(self.points <= -512):
            return 'BOT'
        else:
            None
        # if abs(self.points) < 512:
        #     return False, None
        # else:
        #     if self.points <= -512:
        #         return True, 'BOT'
        #     else:  
        #         return True, 'PLAYER'