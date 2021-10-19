# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final,
# mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

num = []

for i in range(0, 5):
    num.append(int(input('Digite um número: ')))
    if i == 0:
        menor = num[0]
        menor_pos = 0
        maior = num[0]
        maior_pos = num[0]
    else:
        if num[i] < menor:
            menor = num[i]
            menor_pos = i
        elif num[i] > maior:
            maior = num[i]
            maior_pos = i
print(num)
print(f'O valor {maior} na posição {maior_pos+1} é o maior')
print(f'O valor {menor} na posição {menor_pos+1} é o menor')


# num2 = num[:]
# num2.sort()
# print(f'O maior valor é {num2[-1]}')
# print(f'O menor valor é {num2[0]}')
