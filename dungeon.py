# curses is a weird way to manipulate a terminal

# not sure why this needs to be a class, but ok
class Dungeon:
	
	# this first bit is just making a list called self.level that contains strings
	# each string has 7 characters making up one row of the dungeon
	# this list is created each time the class is instantiated
	# e.g. d = dungeon()
	# d.level = this list
 
	def __init__(self):
		self.level =['#######' ,
		 '#.....#' ,
		 '#.....#' ,
		 '#.....#' , 
		 '#.....#' ,
		 '#######' ]


	def drawTo(self, window, x, y):
		# (x, y) will represent the top left of 
		# where we draw
		for row in self.level:
			# moves the cursor to y,x
			window.move(y, x)
			## HELP, how does it know what char and row are??
			for char in row:
				# paint character char at y,x
				# default location of window object if none given
				window.addch(char)
				# HELP, shouldn't you have to add 1 to x after this?
			y += 1
			# start the next row on the next
			# screen row
