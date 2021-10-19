# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso,
# crie duas listas extras que vão conter apenas os valores pares e os valores ímpares
# digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.

num = []


while True:
    num.append(int(input('Digite um número: ')))

    if str(input('Continuar? (S/n) ')).strip().upper()[0] != 'S':
        break


impar = []
par = []

for i in num:
    if i % 2 == 0:
        par.append(i)
    else:
        impar.append(i)

print(f'A lista completa é {num}')
print(f'Números pares: {par}')
print(f'Números ímpares: {impar}')
