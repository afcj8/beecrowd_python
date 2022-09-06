# O tipo de chá, que pode ser: (1) o chá branco; (2) chá verde; (3) chá preto; ou (4) chá de ervas.
# A função count() retorna a quantidade de vezes que um mesmo elemento está contido numa lista.

t = int(input())
a,b,c,d,e = map(int,input().split())

concorrentes = [a,b,c,d,e]
print(concorrentes.count(t))