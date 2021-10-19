# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a 
# quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro 
# custa R$60 por dia e R$0,15 por Km rodado.

dias=float(input('Dias alugados: '))
km=float(input('Km percorridos: '))
pago=60 * dias + .15 * km
print('Valor a pagar: R${:.2f}'.format(pago))