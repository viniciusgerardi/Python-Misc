# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da
# passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

x = float(input('Digite um número: '))

if x <= 200:
    print('{:.2f}'.format(x*.5))
else:
    print('{:.2f}'.format(x*.45))
