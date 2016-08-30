from domino_peca import Peca
from domino_peca import Tabuleiro

a = Peca(1,2)
b = Peca(5,2)
c = Peca(1,4)

print 'a => [1|2]'
print 'b => [5|2]'
print 'c => [1|4]'

print 'tabuleiro'
t = Tabuleiro(a)
print t
print '------------------'
print 'b pela esquerda'
t.add('l',b)
print t
print '------------------'
print 'b pela direita'
t.add('r',b)
print t
print '------------------'
print 'c pela direita'
t.add('r',c)
print t
print '------------------'
print 'c pela esquerda'
t.add('l',c)
print t
print '------------------'

