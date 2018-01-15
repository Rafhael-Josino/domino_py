

import socket
import Classes

# Configura o host e a porta usada para estabelecer a conexao
#host = gethostname()
host = ''
port = 25000
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((host,port))

# Escuta o pedido de conexao feito pelo programa domino_player1.py
print 'Esperando conexao'
s.listen(1)
conn, addr = s.accept()

# Avisa quando a conexao foi feita
print 'Player connected by', addr

# Tentar fazer primeira recepcao de dado fora do while
# First data is randomSeed
data = conn.recv(32)
print 'randomSeed received: ', data
player2, table = Classes.newGame(2, int(data))

# Prints game for Player2
print 'Table:'
print table
print '-------------------------------------'
print 'Player 2'
print player2

# Laco de manutencao da conexao
while 1:
	# Choses piece and send the info to Player 1
	data = input('Chose piece: ')
	conn.sendall(str(data))

	print 'Aguardando por resposta do Jogador 1'

	# Se o dado recebido for '9', encerra a comunicacao
	if data == '9':
		break
	
	# Recebe dado do Jogador 1
	data = conn.recv(32)
	if not data: break
	print 'Dado recebido: ', repr(data)


# Encerra a conexao e fecha o socket
conn.close()
s.close()
