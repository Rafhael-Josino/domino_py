# -*- coding: utf-8 -*-
'''
  Domino classes


  Author	: Rafhael
  Introduced	: 2016-08-30

-------------------------------------------------------------------------------

  TODO:
	- test methods ret
	- make more tests with function checkGame

  CHANGELOG:
	(2018-01-15)	Rafhael
		- method alfaOmega removed
		- attribute Piece.number -> Piece.a & Piece.b
		- method Board.add & function checkGame updated

	(2018-07-01)	Rafhael
		- introduced method from Board: ret & alfaOmega
		- introduced function checkGame

	(2018-01-01)	Rafhael
		- funtion  NewGame returns both Player's pieces and game's table as Board elements

	(2017-12-31)	Rafhael
		- inserted seed parameter in NewGame function to shuffle the Piece elements

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


import random

#################################################
### Classes 
#################################################

class Piece:
	def __init__(self, a, b):
		'''
		Initialize a Piece instance.
	
		Piece((a,b)) represents the piece of domino:

                                   [a,b]
		'''

		self.a = a
		self.b = b

	def __str__(self):
		'''Prints the object likewise a physical piece of domino'''
		return 	"[" + str(self.a) + \
			"|" + str(self.b) + "]"

	def rotate(self):
		'''
		Inverts the the numbers of the piece, like the piece was 
		rotated
		'''
		aux = self.a
		self.a = self.b
		self.b = aux

class Board:
	def __init__(self, row):
		'''
		Initialize a Board instance
		'''
		self.row = row

	def __str__(self):
		'''Print a domino board'''
		return str([self.row[i].__str__() 
					for i in range(len(self.row))])

	def __len__(self):
		'''Return the number of pieces on the board'''
		return len(self.row)

	def __getitem__(self, index):
		'''Return a specific piece of the board'''
		return self.row[index]

	def add(self, direction, newPiece):
		'''
		Add a new piece to the board by its begin or its end, checking
		first wether the new piece can be inserted.
		'''
		
		# Inserting by the begin of the row (that is, its left)
		if (direction == 'l') | (direction == 'L'):
			#if newPiece.numbers[1] == self.row[0].numbers[0]:
			if newPiece.b == self.row[0].a:
				self.row.insert(0, newPiece)
			elif newPiece.a == self.row[0].a:
				newPiece.rotate()
				self.row.insert(0, newPiece)
			else:
				print 'Impossible move'

		# Inserting by the end of the row (that is, its right)
		elif (direction == 'r') | (direction == 'R'):
			#if newPiece.numbers[0] == self.row[-1].numbers[1]:
			if newPiece.a == self.row[-1].b:
				self.row.append(newPiece)
			elif newPiece.b == self.row[-1].b:
				newPiece.rotate()
				self.row.append(newPiece)
			else:
				print 'Impossible move'

	def ret(self, select):
		'''
		Takes off a Piece from a player to be inserted in the table
		'''
		for ii in range(len(self.row)):
			return self.row.pop(select - 1)


#################################################
### Functions 
#################################################

def newGame(player, randomSeed):
	'''
	Initiates all the Piece elements, returning an element Board with 
	the piece [6|6] and, depending on which player is, an element Board
	with his respective pieces
	'''
	counter = 0
	pieceList = range(28)	

	# Build list with all the Piece objects 
	for ii in range(7):
		for jj in range(7):
			if jj > ii:
				break
			pieceList[counter] = Piece((ii, jj))
			counter = counter + 1
	
	# Create object Board with piece [6|6] and then shuffle the other 
	# elements 
	table = Board([pieceList.pop()])

	# Shuffles the sequence of pieces according to the parameter randomSeed
	random.seed(randomSeed)
	r = random.random()
	print 'Random seed: ', randomSeed
	print 'Shuffle seed: ', r
	random.shuffle(pieceList, lambda: random.random())

	if player == 1:
		return Board(pieceList[14:27]), table 
	else:
		return Board(pieceList[0:14]), table

	# The player 1 always has the piece [6|6], putted on the game's table

def checkGame(player, table):
	'''Check if the player can make a move on the current table'''

	alfa = table[0].a	# Begin of the table
	omega = table[-1].b	# End of the table

	for ii in range(len(player)):
		# Check by the begin of the table
		if (player[ii].a == alfa) | (player[ii].b == alfa):
			return 1
		# Check by the end of the table
		if (player[ii].a == omega) | (player[ii].b == omega):
			return 1
	# In the case of any piece cannot be inserted on the table
	return 0
