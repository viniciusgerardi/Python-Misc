# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em
# uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os
# valores pares e ímpares em ordem crescente.

números = [[], []]

for i in range(0, 7):
    x = int(input('Digite um número: '))
    if x % 2 == 0:
        números[0].append(x)
    else:
        números[1].append(x)

números[0].sort()
números[1].sort()

print(f'Os números pares são {números[0]}')
print(f'Os números ímpares são {números[1]}')
