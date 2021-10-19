# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
# Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos
# e fechados na ordem correta.

expressão = str(input('Digite uma expressão: '))

parenteses = []

for i in expressão:
    if i == '(':
        parenteses.append('(')
    elif i == ')':
        if len(parenteses) > 0:
            parenteses.pop()
            break
        else:
            parenteses.append(')')

print(len(parenteses))
if len(parenteses) == 0:
    print('Os parenteses estão na ordem correta')
else:
    print('Os parenteses não estão na ordem correta')
