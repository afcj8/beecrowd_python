inicio,fim = map(int,input().split())

if (inicio < fim):
    t = fim - inicio
else:
    t = (24 - inicio) + fim

print("O JOGO DUROU {:d} HORA(S)".format(t))