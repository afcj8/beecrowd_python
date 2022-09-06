tempo = int(input())

horas = tempo // 3600
r = tempo % 3600

minutos = r // 60
segundos = r % 60

print(horas,minutos,segundos, sep=":")  # A função sep="" permite especificar um separador de valores.