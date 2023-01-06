# This is a sample Python script.
# James Simbolon
# Haverford College

import pygame, random
from time import sleep
import Checkers.constants
from Checkers.board import board

constants = Checkers.constants

# starts pygame

# run the game loop
windowSurface = pygame.display.set_mode((constants.Width, constants.Height))
pygame.display.set_caption('Checkers!?!?!?')

checkersBoard = board(windowSurface, constants.Width, constants.Height)


def main():
    pygame.init()
    checkersBoard.initilizePieces()
    updateDisplay(checkersBoard)
    # print(checkersBoard.getGraph())
    FPS = 60
    legalMoves = []
    selectedSquare = None

    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if selectedSquare != None and legalMoves == [] or selectedSquare == None and legalMoves != []:
                legalMoves = []
                selectedSquare = None
            if event.type == pygame.MOUSEBUTTONDOWN:
                if constants.redTurn:

                    pos = event.pos
                    currentSquare = constants.withinWhichSquare(pos)
                    objSquare = checkersBoard.boardSquares[currentSquare]
                    attackMoves = getAttackingMoves()
                    #print('restart attackMoves')
                    advMoves = getAdvancingMoves()

                    advMoveMade = False
                    #normal reset conditions
                    if selectedSquare is not None:
                        for sqSets in legalMoves:
                            sObjSquare = checkersBoard.boardSquares[selectedSquare]
                            #attacking Move
                            if sqSets[0][0] == 'r' and sObjSquare.getHold() is not None and objSquare.getHold() is None:
                                if currentSquare == sqSets[2]:
                                    hop(sObjSquare.getHold().getName(), sqSets[1], currentSquare)
                                    print('hop')

                            #Advancing Move
                            if currentSquare == sqSets and sObjSquare.getHold() is not None and objSquare.getHold() is None:
                                if attackMoves == []:
                                    movePiece(sObjSquare.getHold(), currentSquare)
                                    advMoveMade = True
                                    print('advMove')

                    if selectedSquare is not None and objSquare.getHold() != None:
                        if (objSquare.getHold().getColor() == constants.RED):
                            selectedSquare = currentSquare
                            updateDisplay()
                            legalMoves = displayPossibleMoves(selectedSquare)
                            print('legalMoves: ' + str(legalMoves))

                            #checking if black lost.
                            constants.redTurn = False
                            pygame.display.update()
                            didRedWin()
                            constants.redTurn = True
                    if selectedSquare is None:
                        if objSquare.getHold() != None and objSquare.getColor() != constants.BLUE:
                            selectedSquare = currentSquare
                            #displays possible moves if color == RED
                            if objSquare.getHold().getColor() == constants.RED:
                                legalMoves = displayPossibleMoves(selectedSquare)
                                print('legalMoves: ' + str(legalMoves))
                                print('getAttackingMoves(): ' + str(getAttackingMoves()))
                                pygame.display.update()

                    if advMoveMade:
                        constants.redTurn = False
                        blackTurn()
                        constants.redTurn = True
            if event.type == pygame.QUIT:
                run = False

def blackTurn():
    #print('blackTurn')
    didRedWin()
    madeAdvMove = False
    random.randint(0, 20)
    attackingMoves = getAttackingMoves()
    print('attackingMoves: ' + str(getAttackingMoves()))
    advancingMoves = getAdvancingMoves()
    print('advancingMoves: ' + str(advancingMoves))
    #implimentation: [[specificPiece, attackedPiece, target Square], [...]]
    potentialPieces = []
    potentialMoves = []
    selectedPiece = ''
    if attackingMoves != []:
        for move in attackingMoves:
            potentialPieces.append(move[0])
        selectedPiece = potentialPieces[random.randint(0, len(potentialPieces) - 1)]
        potentialMoves = getAttackingMoves(selectedPiece)
        chosenMove = potentialMoves[random.randint(0, len(potentialMoves) - 1)]
        hop(chosenMove[0], chosenMove[1], chosenMove[2])


    if attackingMoves == [] and len(advancingMoves) != 0:
        for move in advancingMoves:
            if move[1] != []:
                potentialPieces.append(move[0])
        selectedPiece = potentialPieces[random.randint(0, len(potentialPieces) - 1)]
        potentialMoves = getAdvancingMoves(selectedPiece)

        #1 because first value is the piece name

        pM = potentialMoves[1]
        chosenMove = pM[random.randint(0, len(pM) - 1)]
        movePiece(checkersBoard.blackPieces[selectedPiece], chosenMove)
        madeAdvMove = True
    updateDisplay()
    didRedWin()
    if not madeAdvMove:
        blackTurn()


def displayPossibleMoves(square):
    piece = constants.boardSquares[square].getHold().getName()
    allPossibleAttacks = getAttackingMoves()
    possibleAttacks = getAttackingMoves(piece)
    if not possibleAttacks == []:
        # [specificPiece, attackedPiece, target Square]
        for square in possibleAttacks:
            pygame.draw.circle(checkersBoard.surface, constants.GREEN, constants.boardSquares[square[2]].getCenter(),
                               constants.circleSize)
        return possibleAttacks
    else:
        nPot = getAdvancingMoves(piece)[0]
        #print('nPot: ' + str(nPot))

        #if len is one, then it is just the Name since no legal moves exist.
        if allPossibleAttacks == [] and len(nPot) != 1:
            narrowedPot = nPot[1]
            #print('narrowPot: ' + str(narrowedPot))
            for sq in narrowedPot:
                pygame.draw.circle(checkersBoard.surface, constants.GREEN, constants.boardSquares[sq].center,
                                   constants.circleSize)
            return narrowedPot
    return []



def getAdvancingMoves(piece=None):
    board = checkersBoard
    advancingMoves = []

    if constants.redTurn:
        if piece is None:
            for name in board.redPieces:
                locationSquare = board.redPieces[name].getLocationSquare()
                legalMoves = genLegalMoves(locationSquare)
                advancingMoves = advancingMoves + [[name, legalMoves[0]]]
        else:
            locationSquare = board.redPieces[piece].getLocationSquare()
            legalMoves = genLegalMoves(locationSquare)
            advancingMoves = [[piece, legalMoves[0]]]
    # print('advancingMoves: ' + str(advancingMoves))
    if not constants.redTurn:
        if piece is None:
            for name in board.blackPieces:
                locationSquare = board.blackPieces[name].getLocationSquare()
                legalMoves = genLegalMoves(locationSquare)
                advancingMoves = advancingMoves + [[name, legalMoves[0]]]
        else:
            locationSquare = board.blackPieces[piece].getLocationSquare()
            legalMoves = genLegalMoves(locationSquare)
            advancingMoves = [piece, legalMoves[0]]
    return advancingMoves


def getAttackingMoves(piece=None):
    board = checkersBoard
    # implimentation: [([specificPiece, attackedPiece, target Square],[...]]
    attackingMoves = []
    confirmedAMoves = []
    if constants.redTurn:
        if piece is None:
            for name in board.redPieces:
                locationSquare = board.redPieces[name].getLocationSquare()
                legalMoves = genLegalMoves(locationSquare)
                #print('getAttackingMoves owned legalMoves' + str(legalMoves))
                attackingMoves.append([name, legalMoves[1]])
        else:
            locationSquare = board.redPieces[piece].getLocationSquare()
            legalMoves = genLegalMoves(locationSquare)
            attackingMoves.append([piece, legalMoves[1]])
    # print('attackingMoves: ' + str(attackingMoves))
    if not constants.redTurn:
        if piece is None:
            for name in board.blackPieces:
                locationSquare = board.blackPieces[name].getLocationSquare()
                legalMoves = genLegalMoves(locationSquare)
                attackingMoves.append([name, legalMoves[1]])
        else:
            locationSquare = board.blackPieces[piece].getLocationSquare()
            legalMoves = genLegalMoves(locationSquare)
            attackingMoves.append([piece, legalMoves[1]])
    #print('attackingMoves' + str(attackingMoves))
    for pieces in attackingMoves:
        specificPiece = pieces[0]
        pMoves = pieces[1]
        # print (specificPiece)
        # print('sqSets is: ' + str(sqSets))
        #print ('pMoves = ' + str(pMoves))
        for sqSets in pMoves:
            if sqSets != []:
                #print('sqSets: ' + str(sqSets))
                direction = sqSets[1]
                #print('direction: ' + str(direction))

                attackedPiece = sqSets[0]
                #print('attackedPiece: ' + str(attackedPiece))

                potentialSquares = board.getGraph().listNeighbors(board.boardSquares[attackedPiece].getName())

                for sets in potentialSquares:
                    # if it is the right direction and the square is empty
                    if sets[1] == direction:
                        if board.boardSquares[sets[0]].getHold() == None:
                            # confirm the attack.
                            # only looks for connections between squares that exist, because of the graph.
                            # Notated as follows: [specificPiece, attackedPiece, target Square],[]...
                            targetSquare = board.boardSquares[sets[0]].getName()
                            confirmedAMoves = confirmedAMoves + [[specificPiece, attackedPiece, targetSquare]]
        # print ('confirmedAMoves: ' + str(confirmedAMoves))
    return confirmedAMoves


def hop(pieceName, victimLocation, targetSquare):
    if constants.redTurn:
        piece = checkersBoard.redPieces[pieceName]
    else:
        piece = checkersBoard.blackPieces[pieceName]
    movePiece(piece, targetSquare)
    kill(victimLocation)



def genLegalMoves(square):
    if constants.boardSquares[square].color == constants.WHITE:
        # sets 'piece' to the piece selected
        piece = (constants.boardSquares[square].getHold())
        # grabs the direction to move
        direction = piece.getDirection()

        # determines which squares can be moved to
        potentialSquares = checkersBoard.getGraph().listNeighbors(square)
        narrowedPot = []
        potAttack = []

        for sqSets in potentialSquares:
            # cannot equal direction, as you cannot move to blue squares. If I ever get to making chess I can just change this.
            for pDr in direction:
                if pDr in sqSets[1] and sqSets[1] != pDr:
                    if not checkersBoard.boardSquares[sqSets[0]].empty():
                        # if the piece is a red piece
                        if piece.getName() in checkersBoard.redPieces:
                            # print('blackPieces' + str(checkersBoard.blackPieces))
                            if checkersBoard.boardSquares[sqSets[0]].getHold().getName() in checkersBoard.blackPieces:
                                potAttack.append(sqSets)
                        if piece.getName() in checkersBoard.blackPieces:
                            if checkersBoard.boardSquares[sqSets[0]].getHold().getName() in checkersBoard.redPieces:
                                potAttack.append(sqSets)
                    elif checkersBoard.boardSquares[sqSets[0]].empty():
                        narrowedPot.append(sqSets[0])
        return (narrowedPot, potAttack)


def movePiece(piece, square):
    # moves piece to square, removes previous hold
    #needs obj piece
    inSquare = piece.getLocationSquare()
    constants.boardSquares[inSquare].removeHold()
    location = constants.boardSquares[square].getCenter()
    piece.setLocation(location)
    constants.boardSquares[square].hold(piece)
    isKings()


def updateDisplay(board = checkersBoard):
    # updates Display
    for square in constants.boardSquares:
        cSQ = constants.boardSquares[square]
        pygame.draw.rect(cSQ.surface, cSQ.color, cSQ.location)
    for pieces in board.redPieces:
        p = board.redPieces[pieces]
        circle = pygame.draw.circle(p.surface, p.color, p.center, constants.circleSize)
        if p.getKing():
            windowSurface.blit(constants.CROWN, (p.center[0] - (1/2) * constants.CROWNwidth, p.center[1] - (1/2)* constants.CROWNheight))
    for pieces in board.blackPieces:
        p = board.blackPieces[pieces]
        pygame.draw.circle(p.surface, p.color, p.center, constants.circleSize)
        if p.getKing():
            windowSurface.blit(constants.CROWN, (p.center[0] - (1/2)* constants.CROWNwidth, p.center[1] - (1/2) * constants.CROWNheight))
    pygame.display.update()


def kill(square):
    currentSquare = checkersBoard.boardSquares[square]
    piece = currentSquare.getHold()
    pieceName = piece.getName()
    currentSquare.removeHold()
    if pieceName in checkersBoard.redPieces:
        checkersBoard.redPieces.pop(pieceName)
    if pieceName in checkersBoard.blackPieces:
        checkersBoard.blackPieces.pop(pieceName)
def isKings():
    if constants.redTurn:
        for pieceName in checkersBoard.redPieces:
            promotionSquare = checkersBoard.boardSquares[checkersBoard.redPieces[pieceName].getLocationSquare()]
            if (promotionSquare.isPromotionSquare())[0] == True and (promotionSquare.isPromotionSquare())[1] == constants.RED:
                checkersBoard.redPieces[pieceName].turnKing()
    else:
        if not constants.redTurn:
            for pieceName in checkersBoard.blackPieces:
                promotionSquare = checkersBoard.boardSquares[checkersBoard.blackPieces[pieceName].getLocationSquare()]
                if (promotionSquare.isPromotionSquare())[0] == True and (promotionSquare.isPromotionSquare())[1] == constants.BLACK:
                    checkersBoard.blackPieces[pieceName].turnKing()

def didRedWin():
    #if no pieces, no moves.
    print('getAdvancingMoves: ' + str(getAdvancingMoves()))
    print('getAttackingMoves: ' + str(getAttackingMoves()))
    adv = []
    for moves in getAdvancingMoves():
        if moves[1] != []:
            adv.append(moves[1])
    print('adv: ' + str(adv))
    if (adv == [] and getAttackingMoves() == []) or checkersBoard.blackPieces.keys == [] or checkersBoard.redPieces.keys == []:
        print('gotHere1')
        myfont = pygame.font.SysFont('Comic Sans MS', 50)
        if constants.redTurn is True or checkersBoard.redPieces.keys == []:

            windowSurface.blit(myfont.render('Red Lost', False, (200, 200, 0)), (200,0))
            pygame.display.update()
            print('gotHere2')
            sleep(5)
            pygame.quit()
        if constants.redTurn is False or checkersBoard.blackPieces.keys == []:
            windowSurface.blit(myfont.render('Red Won', False, (200, 200, 0)), (200,0))
            pygame.display.update()
            print('gotHere3')
            sleep(5)
            pygame.quit()





if __name__ == "__main__":
    main()
