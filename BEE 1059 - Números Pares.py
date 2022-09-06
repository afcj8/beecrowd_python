# Para percorrer um conjunto de código um determinado número de vezes, pode-se usar a função range().
# A função range() retorna uma sequência de números, começando em 0 por padrão e incrementa em 1 (por padrão) 
# e termina em um número especificado.
# Definição de número par: um número que ao ser dividido por dois têm resto zero.

for i in range(1,101):
    if (i % 2 == 0):
        print(i)