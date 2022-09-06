# Fórmula para calcular o número de diagonais de um polígono:
# d = (n * (n - 3)) / 2
# d = número de diagonais 
# n = número de lados

n = int(input())
d = (n * (n - 3)) / 2
print(int(d))