#Este código verificado se o aluno passou de ano
print('\033[1;43m-----AVALIAÇÃO DE ALUNO-----\033[m')
aluno = str(input('Nome do aluno: ')).strip().upper()
nota1 = float(input('Nota do primeiro ano: '))
nota2 = float(input('Nota segundo ano: '))
nota3 = float(input('Nota terceiro ano: '))
media = (nota1 + nota2 + nota3) / 3
if media < 5:
    nonal = '\033[31mREPROVADO(A)\033[m'
elif 5 <= media <= 7:
    nonal = '\033[33mem RECUPERAÇÃO\033[m'
else:
    nonal = '\033[34mAPROVADO(A)\033[m'
print('O aluno(a) {} teve média de {:.1f}, ele(a) está {}'.format(aluno, media, nonal))
