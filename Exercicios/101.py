# Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o
# ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa
# tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.


def voto(data_nascimento):
    from datetime import date
    idade = date.today().year - data_nascimento
    print(f'A pessoa tem {idade} anos')
    if idade < 16:
        print('Voto negado')
    elif idade < 18 or idade > 65:
        print('Voto opcional')
    else:
        print('Voto obrigatório')


nascimento = int(input('Informe o ano de nascimento: '))
voto(nascimento)
