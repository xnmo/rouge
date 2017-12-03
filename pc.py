import random

class CharacterCreation:
	def __init__(self):
		self.namerequest = 'What, pray tell, is thy name? '
		self.racerequest = "And thine race? "
	def askForName(self, window, x, y):
		window.move(y,x)
		for char in self.namerequest:
			window.addch(char)

	def askForRace(self, window, x, y):
		window.move(y,x)
		for char in self.racerequest:
			window.addch(char)


class PlayerCharacter:
	def __init__(self, name, race):
		self.name = name
		self.race = race
		self.might = random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6)
		self.hope = random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6)
		self.wit = random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6)
		self.luck = random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6)
		self.hitpoints = random.randint(5,  5 + self.might)  
		
		self.info = ['  NAME | ' + self.name,
					 '  RACE | ' + str(self.race),
					 '    HP | ' + str(self.hitpoints),
				     ' MIGHT | ' + str(self.might),
					 '  HOPE | ' + str(self.hope),
					 '   WIT | ' + str(self.wit),
					 '  LUCK | ' + str(self.luck)]	

	def drawTo(self, window, x, y):
		for attribute in self.info:
			window.move(y, x)
			for char in attribute:
				window.addch(char)
			y += 1



