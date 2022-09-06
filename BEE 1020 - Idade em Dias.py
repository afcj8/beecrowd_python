idade = int(input())

ano = idade // 365
r = idade % 365

mes = r // 30
dias = r % 30

print(ano, "ano(s)")
print(mes, "mes(es)")
print(dias, "dia(s)")