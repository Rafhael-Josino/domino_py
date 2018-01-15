# -*- coding: utf-8 -*-
'''
  Domino player1


  Author	: Rafhael
  Introduced	: 2017-12-31

------------------------------------------------------------------------------

  TODO:
	- Implement game interaction
  CHANGELOG:
	(2017-31-12)
		Introduced code
	(2018-01-01)
		Inserted Player 1's parameters and Table's parameters
		First data sent to Player 2 is now the seed used to shuffle the game's pieces 
		Data send buffer increased
'''

import socket
import Classes
import random

# Random seed used to shuffle the game's pieces
digito = random.randint(1,100)

# Generate the Player 1's set of pieces and the game's table, initially with the 
# piece [6|6]
player1, table = Classes.newGame(1, digito)

# Print game for Player1
print 'Table:'
print table
print '-------------------------------------'
print 'Player 1'
print player1

# Configure the host and port 
host = 'localhost'
port = 25000

# Initiates the socket and try stabilish connection with Player 2
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,port))

print 'Digito enviado: ', digito
# Laco de manutencao da conexao
while 1:
	# Send data to Player 2
	# The first data sent is the random seed used here, so the shuffle
	# is the same
	s.sendall(str(digito))

	print 'Waiting answer from Player 2'

	# Receives data from Player 2
  	data = s.recv(32)
	print 'Data received from Player 2: ', repr(data) 

	digito = input('Digito a ser enviado: ')

	# Se o dado enviado for 9, encerra a comunicacao
	if digito == 9:
		break

# Fecha o socket
s.close()
