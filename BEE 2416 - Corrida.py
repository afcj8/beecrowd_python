# c = número de metros
# n = comprimento da pista

c,n = map(int,input().split())
termino = c % n
print(termino)