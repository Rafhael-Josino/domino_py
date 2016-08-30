import socket

digito = '0'

host = 'localhost'
port = 25000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,port))
while 1:
	s.sendall(str(digito))
  	data = s.recv(1)
	print 'Dado recebido: ', repr(data) 
	digito = input('Digito a ser enviado: ')
	if digito == 9:
		break
s.close()
