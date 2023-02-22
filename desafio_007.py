#Programa que tira a média d eum aluno
print('=====Média de aluno=====')
nome = input('Nome do aluno: ')
n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
s = (n1+n2) / 2
print('O aluno, {} teve a média de {:.1f}'.format(nome, s))
