# Dimensões dos contêineres:
# a = largura
# b = comprimento
# c = altura
# Dimensões do navio:
# x = largura
# y = comprimento
# z = altura

a,b,c = map(int,input().split())
x,y,z = map(int,input().split())

qtd_maxima = (x // a) * (y // b) * (z // c)
print(qtd_maxima)