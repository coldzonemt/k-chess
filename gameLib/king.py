class king(object): 
	def __init__(self): 
		#a king doesn't not have points
		self.row = None 
		self.col = None
		self.hasMoved = False

	def move(self, row, col): 
		#determine current location

		#check if new location is valid 

		#update location?  

	def inCheck(self): 
		#determine if king is in check
		#if king is in check, determine legal moves
		#if King is in check and has no legal moves, end the game
		#return -1 if king is not in check and list of legal moves if king is in check
