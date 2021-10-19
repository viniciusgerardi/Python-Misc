# Faça um programa que leia nome e média de um aluno, guardando também a situação em
# um dicionário. No final, mostre o conteúdo da estrutura na tela.

dados = {}


dados['nome'] = str(input('Digite o nome: '))
dados['média'] = float(input('Digite a média: '))
if dados['média'] >= 5:
    dados['situação'] = 'aprovado'
else:
    dados['situação'] = 'reprovado'

print(dados)

for k, v in dados.items():
    print(f'{k} é {v}')
