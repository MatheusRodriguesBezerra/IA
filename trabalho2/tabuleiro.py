class Tabuleiro:
    def __init__(self, game):
        self.game = game

    def getGame(self):
        nTabuleiro = Tabuleiro(self.game)
        return nTabuleiro.game
    
    def showGame(self):
        for i in self.getGame():
            print(i)
