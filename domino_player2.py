import socket
import domino_peca

#host = gethostname()
host = ''
port = 25000
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((host,port))
s.listen(1)
conn, addr = s.accept()
print 'Player connected by', addr
while 1:
	data = conn.recv(1)
	if not data: break
  	#conn.sendall('2')
	print 'Dado recebido: ', repr(data)
	data = input('Digito a ser enviado: ')
	conn.sendall(str(data))
	if data == '9':
		break
conn.close()
s.close()
