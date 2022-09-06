# A função sorted() cria uma nova lista com os mesmos elementos da lista passada, ordenados crescentemente.

l = list(map(int,input().split()))

if (l == sorted(l)):
    print('C')
elif (l == sorted(l, reverse = True)):
    print('D')
else:
    print('N')