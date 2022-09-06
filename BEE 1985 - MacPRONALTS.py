p = int(input())
i = 0
soma = 0

while (p > i):
    i += 1
    a,b = map(int,input().split())
    if (a == 1001):
        c = 1.5 * b
        soma = soma + c
    elif (a == 1002):
        c = 2.5 * b
        soma = soma + c
    elif (a == 1003):
        c = 3.5 * b
        soma = soma + c
    elif (a == 1004):
        c = 4.5 * b
        soma = soma + c
    elif (a == 1005):
        c = 5.5 * b
        soma = soma + c

print('{:.2f}'.format(soma))