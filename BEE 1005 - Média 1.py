n1 = float(input()) # Ler o valor da primeira nota e armazena na variável n1.
n2 = float(input()) # Ler o valor da segunda nota e armazena na variável n2.
media = (n1 * 3.5 + n2 * 7.5) / 11  # Realiza o calculo da média ponderada com pesos 3.5 e 7.5, respectivamente.
print("MEDIA = {:.5f}".format(media))   # Imprime o resultado com 5 casas decimais após a vírgula (valor real).