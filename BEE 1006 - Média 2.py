a = float(input())  # Ler o valor da primeira nota e armazena na variável a.
b = float(input())  # Ler o valor da segunda nota e armazena na variável b.
c = float(input())  # Ler o valor da terceira nota e armazena na variável c.
media = (a * 2 + b * 3 + c * 5) / 10    # Realiza o calculo da média ponderada com pesos 2, 3 e 5, respectivamente.
print("MEDIA = {:.1f}".format(media))   # Imprime o resultado com 1 casa decimal após a vírgula (valor real).