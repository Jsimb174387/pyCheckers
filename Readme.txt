the pygame module is required for the game to run.
Other than that you simply need to run main after opening the project (I do this by double clicking main.py).
That is done with pycharm, haven't tried with other things. 
And after that simply play checkers as red against black. 


inputs are done by clicking on the (your) piece that you wish to move, then selecting the green squares that appear
that demonstrate possible moves. 

Do note I have never played Checkers so if there is a strange obscure rule I have not coded that is why. 
(i.e, "google en passant")

'piece.py' is where I defined what a 'piece' is.
'square.py' is what I defined what a 'square' is. 
'graph.py' is used to make the connections between squares on a board.

Documents may be called Checkers.(something), and are from a time I was trying to be organized. 

'constants.py' was initially intended to just be random constant values I needed throughout,
but ended as a bit more than that. It holds some functions too: such as 'withinWhichSquare',
which given a position returns the square said position is within. Most everything imports constants.py, as 
they all find uses for it. 

'board.py' is the implimentation of a standard checkers/chess board. It keeps track of the red and black pieces, 
and is created from 'squares' in a graph(). It imports 'piece.py', 'square.py', and 'graph.py'.

'main.py' is where I wrote the actual game of Checkers. It imports pygame, sleep (used for giving some time before
the end of the game), constants, and board. 

'oldMain' is what it sounds like: a previous version of main I used, but discarded to be made better.
Thought I would keep it in, but obviously it is outdated and irrelevant. 

Oh, and Crown.png is a little crown I drew for this. 
