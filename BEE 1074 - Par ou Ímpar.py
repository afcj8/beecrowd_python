i = 0
n = int(input())

while (n > i):
    i += 1
    num = int(input())
    if (num != 0): 
        if (num % 2 == 0 and num > 0):
            print('EVEN POSITIVE')
        elif (num % 2 == 0 and num < 0):
            print('EVEN NEGATIVE')
        elif ((num % 2) + 1 != 0 and num > 0):
            print('ODD POSITIVE')
        elif ((num % 2) + 1 != 0 and num < 0):
            print('ODD NEGATIVE')
    else:
        print('NULL')