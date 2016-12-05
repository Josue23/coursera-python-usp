#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math

'''
Exercício 1 - Desafio da vídeo-aula

Como pedido na video-aula desta semana, escreva um programa que calcula as raízes de uma equação do segundo grau.
- O programa deve receber os parâmetros a, b, e c da equação ax2+bx+c, respectivamente, e imprimir o resultado na saída da seguinte maneira:
- Quando não houver raízes reais imprima:
- esta equação não possui raízes reais
- Quando houver apenas uma raiz real imprima:
a raiz desta equação é X
onde X é o valor da raiz
- Quando houver duas raízes reais imprima:
as raízes da equação são X e Y
onde X e Y são os valor das raízes.
- Além disto, no caso de existirem 2 raízes reais, elas devem ser impressas em ordem crescente, ou seja, X deve ser menor ou igual a Y.
'''

a = float(input('Numero: '))
b = float(input('Numero: '))
c = float(input('Numero: '))

delta = b ** 2 - 4 * a * c

if delta == 0:
  raiz1 = ( - b + math.sqrt(delta)) / ( 2 * a )
  print('a raiz desta equação é %f ' %raiz1)
else:
  if delta < 0:
    print('esta equação não possui raízes reais')
  else:
    raiz1 = ( - b + math.sqrt(delta)) / ( 2 * a )
    raiz2 = ( - b - math.sqrt(delta)) / ( 2 * a )
  
    print('as raízes da equação são %.1f e %.1f' %(raiz2, raiz1))




