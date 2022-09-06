# A função min() retorna o menor elemento da lista.
# O método index() retorna o índice em que um valor está armazenado.

n = int(input())
t = list(map(int,input().split()))
menor = min(t)
indice = t.index(menor)
print(indice + 1)