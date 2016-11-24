# import locale

nome = input('Digite o nome do cliente: ')

dataVencimento = input('Digite o dia de vencimento: ')

mesVencimento = input('Digite o mês de vencimento: ')

valor = input('Digite o valor da fatura: ')
# valor = float(valor)
# LOCALE = ('pt_BR', 'UTF-8')
# locale.setlocale(locale.LC_ALL, 'pt_BR.utf8')

print('Olá, %s' % nome)
print('A sua fatura com vencimento em %s de %s no valor de R$ %s está fechada.' % (dataVencimento, mesVencimento, valor))
