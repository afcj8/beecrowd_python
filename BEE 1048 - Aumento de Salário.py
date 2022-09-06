n = float(input())

if (n <= 400):
    reajuste = n * 0.15
if (n > 400 and n <= 800):
    reajuste = n * 0.12
if (n > 800 and n <= 1200):
    reajuste = n * 0.10
if (n > 1200 and n <= 2000):
    reajuste = n * 0.07
if (n > 2000):
    reajuste = n * 0.04

print("Novo salario: {:.2f}".format(n + reajuste))
print("Reajuste ganho: {:.2f}".format(reajuste))
print("Em percentual: {:.0f} %".format((reajuste / n) * 100))