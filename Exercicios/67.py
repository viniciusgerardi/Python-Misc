# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor
# digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.

while True:
    n = int(input('Digite um número: '))
    if n < 0:
        break
    for x in range(1, 11):
        print(f'{x} x {n} = {x*n}')
