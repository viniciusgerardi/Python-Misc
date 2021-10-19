# Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro
# que indique o número a calcular e outro chamado show, que será um valor lógico (opcional)
# indicando se será mostrado ou não na tela o processo de cálculo do fatorial.


def fatorial(número, mostrar=False):
    resultado = 1
    for i in range(número, 0, -1):
        if mostrar:
            print(i, end='')
            resultado *= i
            if i > 1:
                print(' x ', end='')
            else:
                print(f' = {resultado}')
    return resultado


x = fatorial(5, True)

print(x)
