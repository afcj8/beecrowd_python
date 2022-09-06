# A soma das medidas de dois lados de um triângulo é sempre maior que a medida do terceiro lado.

a,b,c = map(float,input().split())

if (a + b > c and a + c > b and b + c > a):
    p = a + b + c
    print("Perimetro = {:.1f}".format(p))
else:
    area = ((a + b) * c) / 2
    print("Area = {:.1f}".format(area))