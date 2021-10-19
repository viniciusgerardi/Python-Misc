# Faça um programa que tenha uma função chamada contador(), que receba três parâmetros:
# início, fim e passo. Seu programa tem que realizar três contagens através da função criada:
# a) de 1 até 10, de 1 em 1
# b) de 10 até 0, de 2 em 2
# c) uma contagem personalizada


def contador(início, fim, passo):
    print(f'Contagem de {início} até {fim} com passo {passo}')
    if fim <= 0:
        fim -= 1
    else:
        fim += 1

    if início > fim:
        passo = -passo

    for i in range(início, fim, passo):
        print(f'{i} ', end='')
    print()
    print()


contador(1, 10, 1)
contador(10, 0, 2)
contador(-10, 10, 2)
