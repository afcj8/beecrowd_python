n = int(input())
rpm = list(map(int,input().split()))
q = 0

for i in range(1,n):
    if (rpm[i - 1] > rpm[i]):
        q = i + 1
        break   # break: antecipa o fim do laço.

print(q)