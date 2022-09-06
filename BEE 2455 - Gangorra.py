p1,c1,p2,c2 = map(int,input().split())

equilibrio1 = p1 * c1
equilibrio2 = p2 * c2

if (equilibrio1 == equilibrio2):
    print(0)
elif (equilibrio1 > equilibrio2):
    print(-1)
else:
    print(1)