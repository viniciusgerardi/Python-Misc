# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista.
# No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

pessoa = []
lista = []
maior = menor = 0
nome_maior = []
nome_menor = []
i = 0

while True:
    pessoa.append(str(input('Digite o nome: ')))
    pessoa.append(float(input('Digite o peso: ')))
    lista.append(pessoa[:])
    if i == 0:
        maior = pessoa[1]
        menor = pessoa[1]
        nome_maior.append(pessoa[0])
        nome_menor.append(pessoa[0])
    elif pessoa[1] < menor:
        menor = pessoa[1]
        nome_menor.clear()
        nome_menor.append(pessoa[0])
    elif pessoa[1] > maior:
        maior = pessoa[1]
        nome_maior.clear()
        nome_maior.append(pessoa[0])
    elif pessoa[1] == menor:
        nome_menor.append(pessoa[0])
    elif pessoa[1] == maior:
        nome_maior.append(pessoa[0])
    pessoa.clear()
    i += 1
    if str(input('Continuar? (S/n) ')).strip().upper()[0] != 'S':
        break


print(f'Foram cadastradas {len(lista)} pessoas')
print(f'As pessoas mais leves são {nome_menor} com {menor}Kg')
print(f'As pessoas mais pesadas são {nome_maior} com {maior}Kg')
