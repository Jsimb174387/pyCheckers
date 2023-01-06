#James Simbolon, Haverford College

# def main():
#     pygame.init()
#     checkersBoard.initilizePieces()
#     updateDisplay(checkersBoard)
#     print(checkersBoard.getGraph())
#     FPS = 60
#     legalMoves = ([],[])
#     selectedSquare = None
#
#     run = True
#     clock = pygame.time.Clock()
#     capturedThisMove = False
#
#     while run:
#         clock.tick(FPS)
#         for event in pygame.event.get():
#             if selectedSquare != None and legalMoves == ([], []):
#                 legalMoves = ([], [])
#                 selectedSquare = None
#             if event.type == pygame.QUIT:
#                 run = False
#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 pos = event.pos
#                 currentSquare = constants.withinWhichSquare(pos)
#
#                 if constants.redTurn:
#                     #print('legalMoves: ' + str(legalMoves) + ' and selectedSquare: ' + str(selectedSquare))
#                     if selectedSquare == None and checkersBoard.boardSquares[currentSquare].empty():
#                         legalMoves = ([],[])
#                         selectedSquare = None
#                     elif selectedSquare is None:
#                         updateDisplay(checkersBoard)
#                         #print(currentSquare)
#                         #ensures there is a piece at the square, and it is red.
#                         if not checkersBoard.boardSquares[currentSquare].empty():
#                             if checkersBoard.boardSquares[currentSquare].getHold().getName() in checkersBoard.redPieces:
#                                 displayPossibleMoves(currentSquare)
#                                 pygame.display.update()
#                                 legalMoves = genLegalMoves(currentSquare)
#                                 selectedSquare = currentSquare
#                                 #print('legalMoves Now: ' + str(legalMoves) + ' and selectedSquare Now: ' + str(selectedSquare))
#                     elif selectedSquare != None and legalMoves != ([],[]):
#                             for moves in legalMoves[0]:
#                                 if currentSquare == moves:
#                                     movePiece(constants.boardSquares[selectedSquare].holding, currentSquare)
#                                     legalMoves = []
#                                     selectedSquare = None
#                                     updateDisplay(checkersBoard)
#                                     if not capturedThisMove:
#                                         constants.redTurn = False
#                                         blackTurn()
#
#
