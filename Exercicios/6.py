# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
n=int(input('Digite um número: '))
print('O dobro é: ' + str(n))
print('O triplo é: ' + str(n * 3))
print('A raiz quadrada é: {}'.format(str(pow(n,1/2))))