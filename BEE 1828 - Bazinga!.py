i = 0
n = int(input())

while (n > i):
    i += 1
    s,r = map(str,input().split())
    if (s == r):
        print('Caso #{}: De novo!'.format(i))
    elif (s == 'tesoura' and r == 'papel'):
        print('Caso #{}: Bazinga!'.format(i))
    elif (s == 'papel' and r == 'pedra'):
        print('Caso #{}: Bazinga!'.format(i))
    elif (s == 'pedra' and r == 'lagarto'):
        print('Caso #{}: Bazinga!'.format(i))
    elif (s == 'lagarto' and r == 'Spock'):
        print('Caso #{}: Bazinga!'.format(i))
    elif (s == 'Spock' and r == 'tesoura'):
        print('Caso #{}: Bazinga!'.format(i))
    elif (s == 'tesoura' and r == 'lagarto'):
        print('Caso #{}: Bazinga!'.format(i))
    elif (s == 'lagarto' and r == 'papel'):
        print('Caso #{}: Bazinga!'.format(i))
    elif (s == 'papel' and r == 'Spock'):
        print('Caso #{}: Bazinga!'.format(i))
    elif (s == 'Spock' and r == 'pedra'):
        print('Caso #{}: Bazinga!'.format(i))
    elif (s == 'pedra' and r == 'tesoura'):
        print('Caso #{}: Bazinga!'.format(i))
    else:
        print('Caso #{}: Raj trapaceou!'.format(i))