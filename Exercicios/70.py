# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se
# o usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.

preço_mais_barato = 0
quantidade = 0
total = 0
preço1000 = 0

while True:

    produto = str(input('Digite o produto: ')).strip()
    preço = float(input('Digite o preço: R$'))
    quantidade += 1

    if quantidade == 1 or preço < preço_mais_barato:
        preço_mais_barato = preço
        produto_mais_barato = produto

    total += preço
    if preço > 1000:
        preço1000 = +1

    if str(input('Continuar? (S/n): ')).strip().upper()[0] != 'S':
        break

print(f'O total gasto foi R${total:.2f}')
print(f'Foram {preço1000} produtos mais caros que R$1000')
print(
    f'O produto mais barato foi {produto_mais_barato}, custando {preço_mais_barato}')
