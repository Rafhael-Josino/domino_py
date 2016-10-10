# -*- coding: utf-8 -*-
'''
  Domino classes


  Author	: Rafhael
  Introduced	: 2016-08-30

-------------------------------------------------------------------------------

  TODO:
	- finish ret() function
	- insert comments
	- change the name array

  CHANGELOG:
	(2016-10-10)	Rafhael
		- file renamed: domino_peca -> Classes
		- restructured __init__() of Tabuleiro and Peca classes
		- introduced __getitem()__ and __len()__ in Tabuleiro class
		- names changed: Peca -> Piece and Tabuleiro -> Board
		- removed class Carreira

	(2016-09-27)	Rafhael
		- introduced first version of HEADER, TODO and CHANGELOG
		- formating of code for a better looking
	
	(2016-08-30)	Rafhael
		- introduced code of classes
'''

class Piece
	def __init__(self, simbol, num_id):
		self.num_left = simbol[0]
		self.num_right = simbol[1]
		self.num_id = num_id

	def __str__(self):
		return (" [" + str(self.num_left) + 
			"|" + str(self.num_right) + "] ")

	def rotate(self):
		aux = self.num_left
		self.num_left = self.num_right
		self.num_right = aux

class Board:
	def __init__(self):
		self.array = []

	def __str__(self):
		return str([self.array[i].__str__() 
					for i in range(len(self.array))])

	def __len__(self):
		return len(self.array)

	def __getitem__(self, index):
		return self.array[index]


	def add(self, direction, new_peca):
		if (direction == 'l') | (direction == 'e'):
			if new_peca.num_right == self.array[0].num_left:
				self.array.insert(0,new_peca)
			elif new_peca.num_left == self.array[0].num_left:
				new_peca.rotate()
				self.array.insert(0,new_peca)
			else:
				print 'Impossible move'
		elif (direction == 'r' | direction == 'd'):
			if new_peca.num_left == self.array[-1].num_right:
				self.array.append(new_peca)
			elif new_peca.num_right == self.array[-1].num_right:
				new_peca.rotate()
				self.array.append(new_peca)
			else:
				print 'Impossible move'

	def add2(self, new_peca):
		self.array.append(new_peca)

	def ret(self, num_id):
		for ii in range(len(self.array)):
			if self.array[ii].num_id == num_id:
				pass

def new_game():
	num_id = 0
	game = Board()
	for ii in range(7):
		for jj in range(7):
			if jj > ii:
				break
			mesa.add2(Piece((ii, jj), num_id))
			num_id = num_id + 1
	return game
