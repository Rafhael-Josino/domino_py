# -*- coding: utf-8 -*-
'''
  Domino classes


  Author	: Rafhael
  Introduced	: 2016-08-30

-------------------------------------------------------------------------------

  TODO:
	- finish ret() function
	- separe result of newGame() in two parcels randomly generated
	- change Board constructor and remove add2() function 

  CHANGELOG:
	(2016-11-20)	Rafhael
		- comments and descriptions inserted
		- changed variables names to a better format
		- changed parameters of Piece constructor

	(2016-10-11)	Rafhael
		- renamed: self.array -> self.row
		- funtion newGame() now returns a shuffled Board object

	(2016-10-10)	Rafhael
		- file renamed: domino_peca -> Classes
		- restructured __init__() of Tabuleiro and Peca classes
		- introduced __getitem()__ and __len()__ in Tabuleiro class
		- renamed: Peca -> Piece and Tabuleiro -> Board
		- removed class Carreira

	(2016-09-27)	Rafhael
		- introduced first version of HEADER, TODO and CHANGELOG
		- formating of code for a better looking
	
	(2016-08-30)	Rafhael
		- introduced code of classes
'''


from random import shuffle

#################################################
### Classes 
#################################################

class Piece:
	def __init__(self, numbers, numID):
		'''
		Initialize a Piece instance.
	
		Piece((a,b), Id) represents the piece of domino:

                                         [a,b]

		Id is used to indicate which piece is this inside a Board 
		instance
		'''

		self.numbers = numbers
		self.numID = numID

	def __str__(self):
		'''Prints the object likewise a physical piece od domino'''
		return 	"[" + str(self.numbers[0]) + \
			"|" + str(self.numbers[1]) + "]"

	def rotate(self):
		'''
		Inverts the the numbers of the piece, like the piece was 
		rotated
		'''
		self.numbers = self.numbers[::-1]


class Board:
	def __init__(self):
		'''
		Initialize a Board instance
		'''
		self.row = []

	def __str__(self):
		return str([self.row[i].__str__() 
					for i in range(len(self.row))])

	def __len__(self):
		return len(self.row)

	def __getitem__(self, index):
		return self.row[index]

	def add(self, direction, newPiece):
		if (direction == 'l') | (direction == 'L'):
			if newPiece.numbers[1] == self.row[0].numbers[0]:
				self.row.insert(0, new_peca)
			elif newPiece.numbers[0] == self.row[0].numbers[0]:
				newPiece.rotate()
				self.row.insert(0, newPiece)
			else:
				print 'Impossible move'
		elif (direction == 'r') | (direction == 'R'):
			if newPiece.numbers[0] == self.row[-1].numbers[1]:
				self.row.append(new_peca)
			elif newPiece.numbers[1] == self.row[-1].numbers[1]:
				newPiece.rotate()
				self.row.append(newPiece)
			else:
				print 'Impossible move'

	def add2(self, newPiece):
		self.row.append(newPiece)

	def ret(self, numID):
		for ii in range(len(self.row)):
			if self.row[ii].numID == numID:
				pass

	def randomize(self):
		shuffle(self.row)


#################################################
### Functions 
#################################################

def newGame():
	numID = 0
	game = Board()
	for ii in range(7):
		for jj in range(7):
			if jj > ii:
				break
			game.add2(Piece((ii, jj), numID))
			numID = numID + 1
	game.randomize()
	return game
