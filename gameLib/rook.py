class rook(object): 
	def __init__(self): 
		self.points = 5
		self.row = None
		self.col = None
		self.hasMoved = False

	def move(self, row, col): 
		#Make sure the new position contains either the same row or same column