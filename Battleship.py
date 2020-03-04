class Game():
    def __init__(self):
        self.player1 = Player()
        self.player2 = Player()
        self.turn = 0

    def startGame(self):
        continuePlay = "Y"
        while continuePlay == "Y":
            while self.player1.fleetStatus() and self.player2.fleetStatus():
                self.playTurn()
            player1.resetBoard()
            plaayer2.resetBoard()
            continuePlay = input("Play another game? (Y/N): ").upper()

    def displayScore(self):
        pass

    def _updateScore(self):
        pass

    def playTurn(self):
        if self.turn % 2 == 0:
            while True:
                move = self.player1.getMove()
                if self.player2.board.check_move(move):
                    break
                print ("Already shot there")
        else:
            while True:
                move = self.player2.getMove()
                if self.player1.board.check_move(move):
                    break
                print ("Already shot there")
        self.turn += 1

class Player():
    def __init__(self):
        self.score = 0
        self.board = Board()

    def updateScore(self):
        pass

    def resetBoard(self):
        self.board = Board()

    def getMove(self):
        move = input("Where would you like to attack? 'A-H 1-8': ").split(" ")
        move[0] = 65 - ord(move[0].upper())
        move[1] = int(move[1]) - 1
        return move
    
    def fleetStatus(self):
        return self.board.fleet.fleetStatus()

class Board():
    def __init__(self):
        self.boardGrid = [["."] * 8] * 8
        self.fleet = Fleet()

    def printBoard(self):
        print ("   A  B  C  D  E  F  G  H")
        for index, row in enumerate(self.boardGrid):
            print (index + 1, " " + "  ".join(row))

    def updateBoard(self, cordTuple):
        pass

    def check_move(self, moveTuple):
        pass

    def placeShips(self):
        pass 

class Fleet():
    def __init__(self):
        self.battleship = Battleship()
        self.destroyer = Destroyer()
        self.minesweeper1 = Minesweeper()
        self.minesweeper2 = Minesweeper()
    
    def fleetStatus(self):
        shipsStatus = [self.battleship.isSunk, self.destroyer.isSunk, self.minesweeper1.isSunk, self.minesweeper2.isSunk]
        return not all(shipsStatus)
    
class Ship():
    SIZE = 0
    ICON = "0"
    def __init__(self):
        self.health = [self.ICON] * self.SIZE
        self.isSunk = False

    def updateHealth(self, hitIndex):
        if self.health[hitIndex] == "X":
            return print ("Already hit there!")
        self.health[hitIndex] = "X"
        self.__SinkShip()

    def __SinkShip(self):
        if self.health == ["X"] * self.SIZE:
            self.isSunk = True
            print ("Ship sunk!")

class Battleship(Ship):
    Ship.SIZE = 5
    Ship.ICON = "B"

class Destroyer(Ship):
    Ship.SIZE = 3
    Ship.ICON = "D"

class Minesweeper(Ship):
    Ship.SIZE = 2
    Ship.ICON = "M"

if __name__ == "__main__":
    ms = Minesweeper()
    ms.updateHealth(1)
    game = Game()
    game.player1.board.printBoard()
    game.startGame()
    print ("")

