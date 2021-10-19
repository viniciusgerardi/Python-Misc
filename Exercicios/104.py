# Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante 'a
# função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico.


def leiaInt():
    validado = False
    while not validado:
        t = input('Digite um número inteiro: ')
        if t.isnumeric():
            validado = True
        else:
            print(f'{t} não é um número inteiro')
    return t


print(leiaInt())
