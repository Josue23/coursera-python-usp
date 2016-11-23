
print ('Por favor, entre com o número de segundos que deseja converter: ')
totalSegundos = int(input('Digite a quantidade de segundos: '))

horas = totalSegundos // 3600  # divisão inteira
print ('%d horas ou %d segundos' %(horas, horas * 3600))

segundosRestantes = totalSegundos % 3600 # resto da divisão
print ('%d Segundos restantes ' %segundosRestantes)

minutos = segundosRestantes // 60
print ('%d minutos' %minutos)

segundos = segundosRestantes % 60
print ('%d segundos ' %segundos)

print ('%d horas, %d minutos e %d segundos. ' %(horas, minutos, segundos))
