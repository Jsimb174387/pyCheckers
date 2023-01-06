#James Simbolon, Haverford College

from Checkers.graph import *
from Checkers.square import *
from Checkers.piece import *
constants = Checkers.constants


class board:
    def __init__(self, surface, width, height):
        self.board = graph()
        self.surface = surface
        self.boardSquares = {}
        self.redPieces = {}
        self.blackPieces = {}
        self.letterValues = constants.letterValues


        widthOfSquares = width / 8
        heightOfSquares = height / 8
        count = 0


        #Chess coordinates are used, for the board.
        boardPosNames = ['a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8',
                         'b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8',
                         'c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8',
                         'd1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8',
                         'e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8',
                         'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8',
                         'g1', 'g2', 'g3', 'g4', 'g5', 'g6', 'g7', 'g8',
                         'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'h7', 'h8',]

        #The board is an 8x8 grid.

        #Build the board using a 8x8 graph of squares
        for name in boardPosNames:
            #Finds the position of the top left coordinate to input into location.
            y = self.letterValues[name[0]] * heightOfSquares
            x = (int(name[1])-1) * widthOfSquares

            #Creates rectange by (top left x, top left y, width, height).
            location = [x, y, widthOfSquares, heightOfSquares]

            #when both coordinate info matches one another's pos/neg, the square should be BLUE. Otherwise, it
            #needs to be WHITE.
            colorPicker = [self.letterValues[name[0]]+1, int(name[1])]
            color = constants.WHITE
            if colorPicker[0] % 2 == 1 and colorPicker[1] % 2 == 1:
                color = constants.BLUE
            if colorPicker[0] % 2 == 0 and colorPicker[1] % 2 == 0:
                color = constants.BLUE
            self.boardSquares[name] = square(name, color, location, surface)
            self.board.addNode(self.boardSquares[name])
            if name in constants.redPromotionSquares:
                self.boardSquares[name].setAsPromotionSquare(constants.RED)
            else:
                if name in constants.blackPromotionSquares:
                    self.boardSquares[name].setAsPromotionSquare(constants.BLACK)

            #b2
        constants.boardSquares = self.boardSquares

        #Builds connections between squares
        for squares in self.boardSquares:
            numToLetter = {-1: 'fakeKey', 0: 'a', 1: 'b', 2: 'c', 3:'d', 4:'e', 5:'f', 6:'g', 7:'h', 8: 'fakeKey'}

            for count in range (0,2):
                newLetter = numToLetter[self.letterValues[squares[0]] - 1 + count]
                for nextCount in range (0,3):
                    newNumber = str(int(squares[1]) - 1 + nextCount)
                    possibleSquares = '' + newLetter + newNumber
                    if not self.board.connected(squares, possibleSquares):
                        self.board.link(squares, possibleSquares)

    def getGraph(self):
        return self.board

    def initilizePieces(self):

        #Builds the playing position

        rpCount = 1
        for squares in constants.startingPosRed:
            name = ('r' + str(rpCount))
            self.redPieces[name] = piece(name, constants.RED, self.surface, self.boardSquares[squares].center)
            self.boardSquares[squares].hold((self.redPieces[name]))
            rpCount = rpCount + 1

        bpCount = 1
        for squares in constants.startingPosBlack:
            name = ('b' + str(bpCount))
            self.blackPieces[name] = piece(name, constants.BLACK, self.surface, self.boardSquares[squares].center)
            self.boardSquares[squares].hold(self.blackPieces[name])
            bpCount = bpCount + 1
