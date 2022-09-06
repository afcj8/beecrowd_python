i = 0
n = int(input())

while (n > i):
    i += 1
    x,y = map(int,input().split())
    p = (x * y) / 2
    print(int(p), 'cm2')