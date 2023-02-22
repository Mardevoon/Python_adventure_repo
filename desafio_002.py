#Programa que recebe um dado e diz seu tipo
print('Desafio 2: aula 06')
n = input('Digite algo: ')
print(type(n))
print('É um número?', n.isnumeric())
print('É um número com letra?', n.isalnum())
print('É uma letra?', n.isalpha())
print('É deciamal?', n.isdecimal())