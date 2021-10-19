# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

a = int(input('Digite um número: '))
b = int(input('Digite um número: '))
c = int(input('Digite um número: '))


if a > b:
    maior = a
    menor = b
else:
    maior = b
    menor = a


if maior < c:
    maior = c

if menor > c:
    menor = c

print('Maior: {}'.format(maior))
print('Menor: {}'.format(menor))
