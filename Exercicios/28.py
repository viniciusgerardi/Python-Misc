# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça
# para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa
# deverá escrever na tela se o usuário venceu ou perdeu.

import random

aleatorio = random.randint(0,5)

chute=int(input('Digite um número: '))

if aleatorio == chute:
    print('Acertou')
else:
    print('O número era {}'.format(aleatorio))

