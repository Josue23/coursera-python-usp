'''
receba (entrada de dados) o valor correspondente ao lado de um quadrado,
calcule e imprima (saída de dados) seu perímetro e sua área.
'''

lado = int(input('Digite o valor correspondente ao lado de um quadrado: '))

perimetro = lado * 4

area = lado * lado

print('perímetro: %s - área: %s' %(perimetro, area))
