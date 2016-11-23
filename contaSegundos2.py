totalSegundos = int(input('\nPor favor, entre com o número de segundos: '))

dias = totalSegundos // 86400

# verifica se o dia é singular ou plural
if (dias > 1):
    print ('\n%d dias. ' %dias)
else:
    print ('\n%d dia. ' %dias)

horas = totalSegundos % 86400 // 3600
print ('%d horas. ' %horas)

minutos = totalSegundos % 3600 // 60
print ('%d minutos. ' %minutos)

# segundos = totalSegundos - (horas * 3600) - (minutos * 60)
segundos = totalSegundos - (dias * 86400) - (horas * 3600) - (minutos * 60)
print ('%d segundos. ' %segundos)

print ('%d dias, %d horas, %d minutos e %d segundos. ' %(dias, horas, minutos, segundos))
