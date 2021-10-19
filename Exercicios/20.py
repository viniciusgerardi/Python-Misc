# O mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalhos dos
# alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

import random

a=input('Digite o aluno 1: ')
b=input('Digite o aluno 2: ')
c=input('Digite o aluno 3: ')
d=input('Digite o aluno 4: ')

lista= [a, b, c, d]

random.shuffle(lista)

print('A ordem é:')
print(lista)