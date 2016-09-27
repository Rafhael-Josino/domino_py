#Classes to domino game --by Rafhael

class Peca:
	def __init__(self, num_left, num_right, num_id):
		self.num_left = num_left
		self.num_right = num_right
		self.num_id = num_id

	def __str__(self):
		return " [" + str(self.num_left) + "|" + str(self.num_right) + "] "

	def __call__(self):
		return " [" + str(self.num_left) + "|" + str(self.num_right) + "] "

	def rotate(self):
		aux = self.num_left
		self.num_left = self.num_right
		self.num_right = aux

class Carreira(Peca):
	def __init__(self,num_left,num_right):
		Peca.__init__(self,num_left,num_right)

class Tabuleiro:
	def __init__(self, first):
		self.array = []
		self.array.append(first)

	def add(self, direction, new_peca):
		if (direction == 'l') | (direction == 'e'):
			if new_peca.num_right == self.array[0].num_left:
				self.array.insert(0,new_peca)
			elif new_peca.num_left == self.array[0].num_left:
				new_peca.rotate()
				self.array.insert(0,new_peca)
			else:
				print 'Invalide move'
		elif (direction == 'r' | direction == 'd'):
			if new_peca.num_left == self.array[-1].num_right:
				self.array.append(new_peca)
			elif new_peca.num_right == self.array[-1].num_right:
				new_peca.rotate()
				self.array.append(new_peca)
			else:
				print 'Ivalide move'

	def add2(self, new_peca):
		self.array.append(new_peca)

	def __str__(self):
		return str([self.array[i].__str__() for i in range(len(self.array))])

	def ret(self, num_id):
		for i in range(len(self.array)):
			if self.array[i].num_id == num_id:
				pass

	#def __getitem__(self,index):

def new_game():
	num_id = 0
	mesa = Tabuleiro(Peca(0,0,0))
	for i in range(8):
		for j in range(8):
			if j > i:
				break
			mesa.add2(Peca(i,j,num_id))
			num_id = num_id + 1
	return mesa
