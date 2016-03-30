class bishop(object):
	def __init__(self): 
		self.points = 3
		self.row = None
		self.col = None
		self.hasMoved = False

	def move(self, row, col):