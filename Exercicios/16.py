# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção
# Inteira.

import math

x=float(input('Digite um número: '))


print('A parte inteira é {}'.format(math.trunc(x)))