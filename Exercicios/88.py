# Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai
# perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada
# jogo, cadastrando tudo em uma lista composta.

from random import randint

números = []
jogos = 0

while jogos <= 0:
    jogos = int(input('Quantos jogos? '))

for i in range(0, jogos):
    números.append([0, 0, 0, 0, 0, 0])
    for j in range(0, 6):
        x = 0
        while x in números[i]:
            x = randint(1, 60)
        números[i][j] = x

    print(f'O jogo {i+1} é: ', end='')
    números[i].sort()
    for j in range(0, 6):
        print(f'{números[i][j]:>2} ', end='')
    print()
