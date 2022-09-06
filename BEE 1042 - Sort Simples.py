# O tipo list permite a manipulação de coleções.
# A função sort() ordena os elementos de forma crescente, trocando os elementos de índice entre si.

a,b,c = list(map(int,input().split()))
lista = [a,b,c]
l = lista.sort()

print(lista[0])
print(lista[1])
print(lista[2])
print("")
print(a)
print(b)
print(c)