# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

n = int(input('Digite um número: '))
primo = True

if n % 2 == 0:
    primo = False
else:
    for x in range(1, n-1):
        if n % x == 0:
            primo = False

if primo:
    print('É primo')
else:
    print('Não é primo')
