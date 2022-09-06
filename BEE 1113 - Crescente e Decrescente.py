x,y = map(int,input().split())
if (x > y):
    print('Decrescente')
if (x < y):
    print('Crescente')

while (x != y):
    x,y = map(int,input().split())
    if (x > y):
        print('Decrescente')
    if (x < y):
        print('Crescente')