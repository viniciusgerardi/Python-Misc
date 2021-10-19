# Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte
# ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar
# quantas cédulas de cada valor serão entregues.
# OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

valor = int(input('Digite o valor: R$ '))
n50 = n20 = n10 = n1 = 0


while valor >= 50:
    valor -= 50
    n50 += 1
while valor >= 20:
    valor -= 20
    n20 += 1
while valor >= 10:
    valor -= 10
    n10 += 1
while valor >= 1:
    valor -= 1
    n1 += 1


print(f'Foram {n50} x 50') if n50 > 0 else ''
print(f'Foram {n20} x 20') if n20 > 0 else ''
print(f'Foram {n10} x 10') if n10 > 0 else ''
print(f'Foram {n1} x 1') if n1 > 0 else ''
