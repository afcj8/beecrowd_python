n = int(input())
consumo = 7

if n <= 10:
    valor = consumo
elif n <= 30:
    valor = (n - 10)* 1 + consumo
elif n <= 100:
    valor = (n - 30) * 2 + consumo + 20
else:
    valor = (n - 100) * 5 + consumo + 20 + 140

print(valor)