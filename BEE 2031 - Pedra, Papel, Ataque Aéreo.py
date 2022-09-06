n = int(input())
i = 0

while (n > i):
    i += 1
    a = str(input())
    b = str(input())

    if (a == 'ataque' and b == 'pedra'):
        print('Jogador 1 venceu')
    elif (a == 'pedra' and b == 'ataque'):
        print('Jogador 2 venceu')
    elif (a == 'pedra' and b == 'papel'):
        print('Jogador 1 venceu')
    elif (a == 'papel' and b == 'pedra'):
        print('Jogador 2 venceu')
    elif (a == 'ataque' and b == 'papel'):
        print('Jogador 1 venceu')
    elif (a == 'papel' and b == 'ataque'):
        print('Jogador 2 venceu')
    elif (a == 'papel' and b == 'papel'):
        print('Ambos venceram')
    elif (a == 'pedra' and b == 'pedra'):
        print('Sem ganhador')
    elif (a == 'ataque' and b == 'ataque'):
        print('Aniquilacao mutua')