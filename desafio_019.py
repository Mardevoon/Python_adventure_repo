#Este código recebe o nome de quatro alunos e sorteia um para ser sacrificado
from random import choice
n0 = input('Primeiro aluno: ')
n1 = input('Segundo aluno: ')
n2 = input('Terceiro aluno: ')
n3 = input('Quarto aluno: ')
lista = [n0, n1, n2, n3]
sac = choice(lista)
print('O aluno a ser sacrificado foi {}'.format(sac))