from Classes import Piece
from Classes import Board
from Classes import Player
from Classes import checkGame

a = Piece(1,2)
b = Piece(5,2)
c = Piece(1,4)
d = Piece(5,3)
e = Piece(2,4)

print 'a =>', a
print 'b =>', b
print 'c =>', c 
print 'd =>', d 
print 'e =>', e 

print 'Board'
t = Board([a])
print t
print '------------------'
print 'b by the left'
key = t.add('l',b)
print key
print t
print '------------------'
print 'b by the right'
key = t.add('r',b)
print key
print t
print '------------------'
print 'c by the right'
key = t.add('r',c)
print key
print t
print '------------------'
print 'c by the left'
key = t.add('l',c)
print key
print t
print '------------------'
print 'd by the right'
key = t.add('r',d)
print key
print t
print '------------------'
print 'e by the left'
key = t.add('l',e)
print key
print t
print '------------------'

# Player instance
player = Player([Piece(2,2),Piece(6,6)])
player.printPlayer(1)

if checkGame(player, t):
	print 'Possible'
	
else:
	print 'Impossible'


