a,b,c,d = map(int,input().split())

somaCD = c + d
somaAB = a + b

# Utiliza-se as condicionais (if, else, elif),
# para verificar uma expressão e executar um bloco de código caso a condição definida seja verdadeira.

if (b > c and d > a and somaCD > somaAB and c > 0 and d > 0 and a % 2 == 0):
    print("Valores aceitos")
else:
    print("Valores nao aceitos")