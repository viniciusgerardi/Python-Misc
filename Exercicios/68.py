# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando
# o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint

vitórias = 0
poi = ' '

while True:
    while poi not in 'pi':
        poi = str(input('Par ou ímpar? (p/i): ')).strip().lower()[0]
    n1 = int(input('Digite um número: '))
    n2 = randint(0, 10)
    print(f'Escolhi {n2}')
    soma = n1+n2
    if soma % 2 == 0:
        if poi == 'p':
            print(f'Você ganhou! {soma} é par')
            vitórias += 1
        else:
            print(f'Você perdeu! {soma} é par')
            break
    else:
        if poi == 'i':
            print(f'Você ganhou! {soma} é ímpar')
            vitórias += 1
        else:
            print(f'Você perdeu! {soma} é ímpar')
            break

print(f'Você ganhou {vitórias} vezes')
