#James Simbolon, Hav    erford College

import Checkers.constants

constants = Checkers.constants


class piece:
    def __init__(self, name, color, surface, center):
        #print(name)
        self.color = color
        self.king = False
        self.surface = surface
        self.center = center
        self.name = name

        self.circle = (surface, color, center, constants.circleSize)
        if self.color == constants.RED:
            self.direction = constants.north
        if self.color == constants.BLACK:
            self.direction = constants.south

        #print(self.getLocationSquare())
    def getColor(self):
        return self.color

    # def movePiece(self, square):
    #     # precondition: give it the name of the square to move to
    #     if constants.boardSquares[square].empty():
    #         constants.boardSquares[square].hold(self)
    #         self.circle.move(self, constants.boardSquares[square].center)

    def turnKing(self):
        self.king = True
        self.direction = constants.south + constants.north

    def getKing(self):
        return self.king

    def getDirection(self):
        return self.direction

    def setLocation(self, newCenter):
        self.center = newCenter
    def getLocationSquare(self):
        return constants.withinWhichSquare(self.center)
    def getName(self):
        #print(self.name)
        return self.name

    def __repr__(self):
        return self.circle
