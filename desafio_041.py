#Este código determina a categoria de um atleta segundo sua idade
from datetime import date
print('CONFEDERAÇÃO NACIONAL DE NATAÇÃO')
print('Digite a idade do atleta para saber sua categoria')
ano = int(input('Ano de nascimento do atleta: '))
idade = date.today().year - ano
print('Idade no atleta: \033[33m{} anos\033[m'.format(idade))
if idade <= 9:
    classificacao = 'MIRIM'
elif idade <= 14:
    classificacao = 'INFANTIL'
elif idade <= 19:
    classificacao = 'JUNIOR'
elif idade <= 25:
    classificacao = 'SÊNIOR'
else:
    classificacao = 'MASTER'
print('Classificação: \033[36m{}\033[m'.format(classificacao))
