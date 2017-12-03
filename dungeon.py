class Dungeon:
	
	def __init__(self):
		self.level =['#######' ,
		 '#.....#' ,
		 '#.....#' ,
		 '#.....#' , 
		 '#.....#' ,
		 '#######' ]


	def drawTo(self, window, x, y):
		for row in self.level:
			window.move(y, x)
			for char in row:
				window.addch(char)
			y += 1
