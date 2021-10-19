# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
# Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos
# e fechados na ordem correta.

expressão = str(input('Digite uma expressão: '))

aberto = False
erro = False

for i in expressão:
    if (i == '(' and aberto) or (i == ')' and not aberto):
        erro = True
        break
    elif i == '(':
        aberto = True
    elif i == ')':
        aberto = False

if erro:
    print('Os parenteses não estão na ordem correta')
else:
    print('Os parenteses estão na ordem correta')
