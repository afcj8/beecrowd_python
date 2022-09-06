i = 0
n = int(input())

while (n > i):
    i += 1
    entrada = input().split()
    nome = str(entrada[0])
    forca = int(entrada[1])
    if (nome == 'Thor'):
        print('Y')
    else: 
        print('N')