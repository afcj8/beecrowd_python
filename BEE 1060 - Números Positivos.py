# A declaração while cria um laço que executa uma instrução (ou um conjunto de instruções) especifícas,
# enquanto a condição de teste for avaliada como verdadeira.

c = 0   # Contador dos números positivos
i = 0   # Contador de iteração

while (i < 6):  # (i < 6) ---> condição
    i += 1  # Incremento de iteração
    x = float(input())
    if (x > 0):
        c += 1  # Incremento dos números positivos

print('{} valores positivos'.format(c))