
totalSegundos = int(input('Por favor, entre com o número de segundos: '))

horas = totalSegundos // 3600
print ('%d horas ' %horas)

minutos = totalSegundos % 3600 // 60
print ('%d minutos ' %minutos)

segundos = totalSegundos - (horas * 3600) - (minutos * 60)
print ('%d segundos ' %segundos)

print ('%d horas, %d minutos e %d segundos. ' %(horas, minutos, segundos))
