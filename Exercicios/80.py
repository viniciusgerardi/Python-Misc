# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os
# em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre
# a lista ordenada na tela.

num = []
i = 0

for i in range(0, 5):
    x = int(input('Digite um número: '))
    if i == 0:
        num.append(x)
    else:
        for j in range(0, len(num)+1):
            if j == len(num):
                num.append(x)
            elif x < num[j]:
                num.insert(j, x)
                break


print(num)
