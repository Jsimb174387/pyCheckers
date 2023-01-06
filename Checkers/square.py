# James Simbolon, Haverford College
import Checkers.constants

constants = Checkers.constants


class square:
    def __init__(self, name, color, location, surface):
        self.rect = (surface, color, location)
        self.color = color
        self.surface = surface
        self.name = name
        self.center = [location[0] + location[2] / 2, location[1] + location[3] / 2]
        self.holding = None
        self.holdingPotential = False
        self.promotionSquare = False
        self.location = location
        self.promotionType = None

    def getName(self):
        return self.name
    def getColor(self):
        return self.color
    def hold(self, obj):
        self.holding = obj

    def getHold(self):
        return self.holding

    def getLocation(self):
        return self.location

    def removeHold(self):

        self.holding = None

    def holdingPotential(self):
        self.holdingPotentail = True

    def getHoldingPotential(self):
        return self.holdingPotential

    def clearPotential(self):
        self.holdingPotential = False

    def isPromotionSquare(self):
        return [self.promotionSquare, self.promotionType]

    def setAsPromotionSquare(self, type):
        self.promotionSquare = True
        self.promotionType = type

    def empty(self):
        return self.holding is None
    def getCenter(self):
        return self.center



