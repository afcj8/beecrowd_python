i = 0
n = int(input())

while (n > i):
    i += 1
    xj,dj = map(int,input().split())
    xj1,dj1 = map(int,input().split())
    xj2,dj2 = map(int,input().split())
    xm,dm = map(int,input().split())
    xm1,dm1 = map(int,input().split())
    xm2,dm2 = map(int,input().split())

    pj = (xj * dj) + (xj1 * dj1) + (xj2 * dj2)
    pm = (xm * dm) + (xm1 * dm1) + (xm2 * dm2)

    if (pj > pm):
        print('JOAO')
    else: 
        print('MARIA')