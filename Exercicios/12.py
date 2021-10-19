# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

n=float(input('Preço: '))
print('Preço com desconto: R${:.2f}'.format(n * .95))