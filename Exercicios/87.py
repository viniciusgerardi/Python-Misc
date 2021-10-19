# Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha..

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = 0

for i in range(0, 3):
    for j in range(0, 3):
        matriz[i][j] = int(input(f'Digite o valor para [{i+1},{j+1}]: '))
        if matriz[i][j] % 2 == 0:
            pares += matriz[i][j]

print('A matriz é:')

for i in range(0, 3):
    for j in range(0, 3):
        print(f'{matriz[i][j]} \t', end=' ')
    print()

print(f'A soma dos valores pares é {pares}')

soma3c = 0
for i in range(0, 3):
    soma3c += matriz[i][2]
print(f'A soma dos valores da 3ª coluna é {soma3c}')

maior = 0
for j in range(0, 3):
    if j == 0:
        maior = matriz[1][j]
    elif matriz[1][j] > maior:
        maior = matriz[1][j]
print(f'O maior valor da 2ª linha é {maior}')
