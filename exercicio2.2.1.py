'''
Dada uma sequência de números inteiros diferentes de zero,
terminada por um zero, calcular a sua soma.
'''


def main():
    a = int(input('Número: '))
    soma = 0

    while a != 0:
        soma += a
        a = int(input('Número: '))


    # verifica se a soma é diferente de zero
    if (soma == 0):
        print('Soma: % d ' % soma)
    print('Soma: % d ' % soma)

main()
