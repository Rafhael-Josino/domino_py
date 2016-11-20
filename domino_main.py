from Classes import Piece
from Classes import Board

a = Piece((1,2),0)
b = Piece((5,2),0)
c = Piece((1,4),0)

print 'a =>', a
print 'b =>', b
print 'c =>', c 

print 'Board'
t = Board()
t.add2(a)
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
