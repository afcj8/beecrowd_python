soma = 0
c = 0
i = 0

while (i < 6):
    i += 1
    x = float(input())
    if (x > 0):
        soma = soma + x
        c += 1
        media = soma / c

print('{} valores positivos'.format(c))
print('{:.1f}'.format(media))