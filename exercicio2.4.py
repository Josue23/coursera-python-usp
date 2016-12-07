'''
https://panda.ime.usp.br/aulasPython/static/aulasPython/aula02.html

Dado um número inteiro n >= 0, calcular n!
'''

# define a funcao fatorial
def fatorial():
    n = int(input('Digite n: '))

    if (n >= 0):
        if (n == 0 or n == 1):
            fatorial = 1
        else:
            fatorial = 1
            for i in range(1, n):
                fatorial *= (i + 1)

    print('!%d = %d ' %(n, fatorial))

fatorial()
