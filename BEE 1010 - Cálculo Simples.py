# A função split() permite dividir o conteúdo da variável de acordo com as condições especificadas em cada parâmetro da função. 
# Ou com valores predefinidos por padrão.

peca1 = input().split()
c1 = int(peca1[0])
n1 = int(peca1[1])
v1 = float(peca1[2])

peca2 = input().split()
c2 = int(peca2[0])
n2 = int(peca2[1])
v2 = float(peca2[2])

total = (n1 * v1) + (n2 * v2)
print("VALOR A PAGAR: R$ {:.2f}".format(total))