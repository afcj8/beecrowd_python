c1,c2,c3,c4 = map(int,input().split())

if (c1 == 1 and c2 == 0 and c3 == 0 and c4 == 0):
    print(1)
elif (c1 == 0 and c2 == 1 and c3 == 0 and c4 == 0):
    print(2)
elif (c1 == 0 and c2 == 0 and c3 == 1 and c4 == 0):
    print(3)
else:
    print(4)