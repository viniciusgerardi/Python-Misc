# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

num = []
total = 0

while True:
    num.append(int(input('Digite um número: ')))
    total += 1

    if str(input('Continuar? (S/n) ')).strip().upper()[0] != 'S':
        break

print(f'Foram digitados {total} números')
num.sort()
print(num)

if 5 in num:
    print('Foi digitado 5')
else:
    print('Não foi digitado 5')
