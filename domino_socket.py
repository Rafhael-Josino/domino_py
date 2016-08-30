#A pair (host,port) is used for the AF_INET address family, where host
#is a string:
#	-hostname in interner domain
#	-or an IPv4 address
import socket

class Socket:
  def __init__(self, sock=None):
    if sock is None:
      self.sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    else
      self.sock = sock

  def connect(self, host, port):
    self.sock.connect((host,port))

  def sending(self, msg):
    pass

