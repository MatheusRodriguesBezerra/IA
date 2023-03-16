class Tabuleiro:
    def __init__(self, game):
        self.game = game

    def getGame(self):
        nTabuleiro = Tabuleiro(self.game)
        return nTabuleiro.game
    
    def showGame(self):
        for i in self.getGame():
            print(i)

    def __str__(self):
        string = ""
        for i in self.game:
            string += str(i) + '\n'
        return string
    
    def __eq__(self, other):
        if(type(other) is not Tabuleiro):
            return False
        return self.game == other.game
        
