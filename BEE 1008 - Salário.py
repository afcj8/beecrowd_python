numero = int(input())   # Ler o número do funcionário.
horas = int(input())    # Ler a quantidade de horas trabalhadas.
valor = float(input())  # Ler o valor que o funcionário recebe por hora.
salario = horas * valor # Realiza o cálculo do salário do funcionário.
print("NUMBER = {:d}".format(numero))   # Imprime o número do funcionário, no formato inteiro.
print("SALARY = U$ {:.2f}".format(salario)) # Imprime o valor do salário do funcionário, com 2 casas decimais após a vírgula.