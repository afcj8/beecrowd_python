c,q = map(int,input().split())

if (c == 1):
    total = q * 4
elif (c == 2):
    total = q * 4.5
elif (c == 3):
    total = q * 5
elif (c == 4):
    total = q * 2
elif (c == 5):
    total = q * 1.5

print("Total: R$ {:.2f}".format(total))