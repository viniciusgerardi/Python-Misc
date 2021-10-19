# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa
# que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

import random

a=input('Digite o aluno 1: ')
b=input('Digite o aluno 2: ')
c=input('Digite o aluno 3: ')
d=input('Digite o aluno 4: ')

lista= [a, b, c, d]



x=random.randrange(1, 4)

print('O escolhido é {}'.format(lista[x]))


print('O escolhido é {}'.format(random.choice(lista)))