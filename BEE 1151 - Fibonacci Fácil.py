# A seguinte sequência de números 0 1 1 2 3 5 8 13 21... é conhecida como série de Fibonacci. 
# Nessa sequência, cada número, depois dos 2 primeiros, é igual à soma dos 2 anteriores.
# Fn = Fn - 1 + Fn - 2 ---> Fórmula de Fibonacci.   
# A função len() permite obter a quantidade de elementos armazenados na coleção.
# Utiliza-se o método append() para inserir um elemento no final da lista.

n = int(input())

fib = [0, 1]

while len(fib) < n:
    fib.append(fib[-1] + fib[-2]) # -1 acessa o último elemento, -2 acessa o penúltimo elemento

for i in range(n):
    if i == n - 1:
        print(fib[i], end="\n")
    else:
        print(fib[i], end=" ")