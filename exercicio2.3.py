'''
https://panda.ime.usp.br/aulasPython/static/aulasPython/aula02.html

Dados números inteiros n e k, com k >= 0, calcular n elevado a k.
Por exemplo, dados os números 3 e 4 o seu programa deve escrever o número 81.
'''


def main():
    n = int(input('Digite n: '))
    k = int(input('Digite k: '))

    if (k >= 0):
        result = n ** k
        print('%d ^ %d = %d ' %(n, k, result))
    else:
        print('O expoente deve ser maior ou igual a zero. ')


main()
