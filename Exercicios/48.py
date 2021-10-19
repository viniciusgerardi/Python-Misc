# Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que
# se encontram no intervalo de 1 até 500.

soma=0
contagem=0

for x in range(1,501,2):
    if x%3==0:
        print(x, end=' ')
        soma += x
        contagem += 1
print()
print('A soma dos {} valores é: {}'.format(contagem, soma))
