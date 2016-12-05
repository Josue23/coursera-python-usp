#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Exercício 6 - Verificando ordenação

Receba 3 números inteiros na entrada e imprima

crescente

se eles forem dados em ordem crescente. Caso contrário, imprima

não está em ordem crescente
'''

n1 = int(input('Numero: '))
n2 = int(input('Numero: '))
n3 = int(input('Numero: '))

if (n1 < n2 < n3):
  print('crescente')
else:
  print('não está em ordem crescente')