#Este código adiciona produtos a lista de compra mostrando no final o total da compra
from time import sleep

cont = p = total = a = v_barato = 0
n_barato = ''

print('=' * 23)
print('LOJA CYPERDRAGon')
print('=' * 23)

while True:
    nome = ''
    while not nome:
        nome = str(input('Nome do produto: ')).upper().strip()
    
    while True:
        p = float(input('Valor do produto: R$ '))
        if p >= 1:
            break
        print('\033[1:31m   Nesta loja não existem produtos no valor de R$0\033[m')
        sleep(2)
    total += p
    cont += 1
    if cont == 1 or p < v_barato:
        v_barato = p
        n_barato = nome
    if p >= 1000:
        a += 1
    x = ' '
    while x not in 'SN':
        x = str(input('Continuar comprando? [S/N] ')).upper().strip()[0]
    if x == 'N':
        break

print('{:-^40}'.format('FIM DA COMPRA'))
print(f'\nO valor total da compra foi R$ {total:.2f}')
print(f'Ao total {a} produtos custaram mais de mil reais')
print(f'O produto mais barato foi {n_barato} custando R$ {v_barato:.2f}')
