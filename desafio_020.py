#Este código recebe o nome de quatro alunos e cria uma fila
from random import shuffle
n1 = input('Primeiro aluno: ')
n2 = input('Segundo aluno: ')
n3 = input('Terceiro aluno: ')
n4 = input('Quarto aluno: ')
sacrificios = [n1, n2, n3, n4]
escolha = shuffle(sacrificios)
print('Os alunos irão na seguinte ordem:')
print(sacrificios)
