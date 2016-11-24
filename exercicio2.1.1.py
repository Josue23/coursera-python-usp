# https://panda.ime.usp.br/aulasPython/static/aulasPython/aula02.html


def main():
    # a_str e b_str  guardam strings
    a_str = input('Digite o primeiro número: ')
    b_str = input("Digite o segundo numero: ")

    #  a_int e b_int guardam inteiros
    a_int = int(a_str)  # converte string/texto para inteiro
    b_int = int(b_str)  # converte string/texto para inteiro

    # calcule a soma entre valores que são números inteiros
    soma = a_int + b_int

    # imprima a soma
    print('A soma de %d + %d é igual a %d ' % (a_int, b_int, soma))

main()
