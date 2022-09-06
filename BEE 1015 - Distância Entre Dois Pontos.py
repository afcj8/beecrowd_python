 # Importação da biblioteca math, que fornece acesso as funções matemáticas definidas pelo padrão C.
 # A função math.sqrt() realiza o cálculo da raiz quadrada de um número.

import math

x1,y1 = map(float,input().split())
x2,y2 = map(float,input().split())

distancia = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
print("{:.4f}".format(distancia))