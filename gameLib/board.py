#import the pieces
#do the logic of play here
#make a class for each piece
'''
The board class is where I will store the state of the game. 
There are two properties of the class (so far): the board, and
the number of turns (for determining if it is black or white's 
turn, and one of the draw rules). 
'''

class board(object): 
	def __init__(self): 
		self.board = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'
		#self.board = range(0,63)
		#row = index / 8 
		#col = index % 8
		self.turns = 0

def startGame(): 
	#set up initial board using FEN strings: 


def updateBoard(move): 
	#update the board with new FEN string

def getLocation(loc): 
	#translate FEN string to algebraic notation

