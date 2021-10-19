# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os
# em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final,
# serão exibidos todos os valores únicos digitados, em ordem crescente.

num = []
i = 0

while True:
    x = int(input('Digite um número: '))
    if x not in num:
        num.append(x)
    else:
        print('Repetido')
    if str(input('Continuar? (S/n) ')).strip().upper()[0] != 'S':
        break

num.sort()
print(num)
