# Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros
# com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles
# é o maior.


def maior(*números):
    if len(números) > 0:
        maior = números[0]

        for i in números:
            if i > maior:
                maior = i
        print(
            f'Foram informados {len(números)} números e o maior valor é {maior}')
    else:
        print('Nenhum valor informado')


maior(1, 2, 3, 4, 5, 6, 7, 8, 10)
maior()
