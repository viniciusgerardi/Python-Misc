# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno
# e tangente desse ângulo.

import math

x=float(input('Digite um ângulo: '))


print('o seno é {}'.format(math.sin(math.radians(x))))
print('o cosseno é {}'.format(math.cos(math.radians(x))))
print('a tangente é {}'.format(math.tan(math.radians(x))))