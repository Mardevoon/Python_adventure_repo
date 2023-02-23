#Este código cadastra pessoas, imprimindo determindados dados ao fim
from time import sleep

maior = h = m = 0
while True:
    print('-' * 23)
    print('CADASTRE UMA PESSOA')
    print('-' * 23)
    id = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).upper().strip()[0]
    if id >= 18:
        maior += 1
    if sexo == 'M':
        h += 1
    if sexo == 'F' and id < 20:
        m += 1
    print('-' * 23)
    esc = ' '
    while esc not in 'SN':
        esc = str(input('Quer continuar? [S/N] ')).upper().strip()
    if esc == 'N':
        break
print('=-' * 23)
print(f'\nTotal de pessoal com mais de 18 anos: {maior}')
print(f'Total de homens cadastrados: {h}')
print(f'Total de mulheres com menos de 20 anos cadastradas: {m}')