#James Simbolon, Haverford College
import pygame

# Board
Width, Height = 600, 600
boardSquares = {}
letterValues = {'a': 0, 'b': 1, 'c': 2,'d': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
#letterValues:
#a = 0, b = 1, c = 2, d = 3, e = 4, f = 5, g = 6, h = 7

redTurn = True

#Squares

#technically half of these do not need to be coded, but I might try to make chess in the future, so I'll do it anyways.
northeast = 'NE'
northwest = 'NW'
southeast = 'SE'
southwest = 'SW'
north = 'N'
south = 'S'
east = 'E'
west = 'W'
redPromotionSquares = ['a2', 'a4', 'a6', 'a8']
blackPromotionSquares = ['h1', 'h3', 'h5', 'h7']
def oppositeDirection(direction):
    # only a few options for directions
    if direction == northeast:
        return southwest
    if direction == northwest:
        return southeast
    if direction == southeast:
        return northwest
    if direction == southwest:
        return northeast
    if direction == north:
        return south
    if direction == south:
        return north
    if direction == east:
        return west

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Piece
circleSize = ((Height) /18)
CROWN = pygame.transform.scale((pygame.image.load('Crown.png')), (45, 25))
CROWNwidth = 45
CROWNheight = 25

# starting positions:
startingPosRed = ['h1', 'h3', 'h5', 'h7', 'g2', 'g4', 'g6', 'g8', 'f1', 'f3', 'f5', 'f7']
startingPosBlack = ['a2', 'a4', 'a6', 'a8', 'b1', 'b3', 'b5', 'b7', 'c2', 'c4', 'c6', 'c8']

def withinWhichSquare(tuple):
    #returns the name/key of the square that the coordinates are in.
    x = tuple[0]
    y = tuple[1]
    for square in boardSquares:
        pos = boardSquares[square].getLocation()
        rangeOfX = [pos[0], pos[0] + pos[2]]
        rangeOfY = [pos[1], pos[1] + pos[3]]
        if rangeOfX[0] <= x <= rangeOfX[1] and rangeOfY[0] <= y <= rangeOfY[1]:
            return square