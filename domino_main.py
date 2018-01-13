from Classes import Piece
from Classes import Board

a = Piece((1,2))
b = Piece((5,2))
c = Piece((1,4))
d = Piece((3,5))

print 'a =>', a
print 'b =>', b
print 'c =>', c 
print 'd =>', d 

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
