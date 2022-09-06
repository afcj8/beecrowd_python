def fatorial(n):
    if (n == 0):    # Caso de base
        return 1
    else:
        fat = n * fatorial(n - 1)
        return fat

n = int(input())
x = fatorial(n)
print(x)