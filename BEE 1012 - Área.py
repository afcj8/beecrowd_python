# A função map() mapeia os elementos e aplica uma função a cada item.

# triangulo retangulo = (base * altura) / 2
# circulo = pi * raio^2
# trapezio = ((baseMaior + baseMenor) * altura) / 2
# quadrado = comprimento * largura
# retangulo = comprimento * largura

a,b,c = map(float,input().split())

tri = (a * c) / 2
cir = 3.14159 * c ** 2
tra = ((a + b) * c) / 2
qua = b * b
ret = a * b

print("TRIANGULO: {:.3f}".format(tri))
print("CIRCULO: {:.3f}".format(cir))
print("TRAPEZIO: {:.3f}".format(tra))
print("QUADRADO: {:.3f}".format(qua))
print("RETANGULO: {:.3f}".format(ret))