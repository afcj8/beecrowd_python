tempo_gasto = int(input())
velocidade_media = int(input())
distancia = tempo_gasto * velocidade_media
qtd_litros = distancia / 12
print("{:.3f}".format(qtd_litros))