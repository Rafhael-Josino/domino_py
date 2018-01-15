from Classes import Piece
from Classes import Board
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
t.add('l',b)
print t
print '------------------'
print 'b by the right'
t.add('r',b)
print t
print '------------------'
print 'c by the right'
t.add('r',c)
print t
print '------------------'
print 'c by the left'
t.add('l',c)
print t
print '------------------'
print 'd by the right'
t.add('r',d)
print t
print '------------------'
print 'e by the left'
t.add('l',e)
print t
print '------------------'

player = Board([Piece(2,2),Piece(6,6)])
print 'Player: ', player

if checkGame(player, t):
	print 'Possible'
else:
	print 'Impossible'
