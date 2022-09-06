# l = comprimento da estrada
# d = distância entre pedágios
# k = custo por quilômetro percorrido
# p = valor de cada pedágio

l,d = map(int,input().split())
k,p = map(int,input().split())

x = l * k
y = (l // d) * p
total = int(x + y)
print(total)