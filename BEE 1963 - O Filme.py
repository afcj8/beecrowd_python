# a = valor antigo
# n = valor novo

a,n = map(float,input().split())
aumento = (n * 100 / a) - 100
print("{:.2f}%".format(aumento))