a,b = map(int,input().split())

if (b <= 2):
    print('nova')
if (a < b and b >= 3 and b <= 96):
    print('crescente')
if (b > 96):
    print('cheia')
if (a > b and b <= 96 and b >= 3):
    print('minguante')