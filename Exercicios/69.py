# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa
# deverá perguntar se o usuário quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.

q18 = 0
qh = 0
qm20 = 0

while True:
    idade = int(input('Digite a idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Digete o sexo (M/F): ')).strip().upper()[0]
    if idade > 18:
        q18 += 1
    elif sexo == 'M':
        qh += 1
    elif sexo == 'F' and idade < 20:
        qm20 += 1
    if str(input('Continuar? (S/n)')).strip().upper()[0] != 'S':
        break
print(f'{q18} pessoas com mais de 18 anos')
print(f'{qh} homens')
print(f'{qm20} mulheres com menos de 20 anos')
