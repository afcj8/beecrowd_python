nome = str(input())         # Ler o nome do vendedor.
salario = float(input())    # Ler o valor do salário fixo do vendedor.
vendas = float(input())     # Ler o total de vendas efetuadas por este vendedor.
bonus = vendas * 0.15       # Calcula o bônus de 15% sobre o total de vendas.
total = salario +  bonus    # Calcula a soma do valor total que o funcionário deve receber.
print("TOTAL = R$ {:.2f}".format(total))    # Imprime o valor total com 2 casas decimais após a vírgula.