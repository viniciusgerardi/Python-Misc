# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre
# uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

vel = int(input('Digite a velocidade: '))

if vel > 80:
    print('A multa é de R${:.2f}'.format((vel-80)*7))
else:
    print('Ok')
