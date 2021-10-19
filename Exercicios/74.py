# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior
# valor que estão na tupla.

from random import randint

t = (randint(0, 10), randint(0, 10), randint(
    0, 10), randint(0, 10), randint(0, 10))
u = sorted(t)

print(f'Os valores sorteados foram: {t}')
print(u)
print(f'O maior valor é {u[-1]}')
print(f'O menor valor é {u[0]}')
