entrada = list(input('Digite um número inteiro: '))

if (len(entrada) > 1):
    print ('O dígito das dezenas é %s' %entrada[-2])
else:
    print ('O dígito das dezenas é 0')
