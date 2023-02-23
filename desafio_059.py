'''Este código faz diversas funções com valores inseridos como
  somar, dizer qual é o maior e colocar valores novos'''
import os
from time import sleep

print('Por favor, digite dois valores e escolha uma opção\n')
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))

aceito = False
while not aceito:
    print('''    [ 1 ] SOMAR
    [ 2 ] MULTIPLICAR
    [ 3 ] MAIOR
    [ 4 ] NOVOS VALORES
    [ 5 ] SAIR DO PROGRAMA''')
    esc = int(input('>>>Opção: '))
    if esc < 1 or esc > 5:
        print('Opção {} INVÁLIDA. Escolha entre 1 e 5'.format(esc))
    else:
        if esc == 1:
            print('Opção SOMAR escolhida:')
            print('{} + {} = {}'.format(n1, n2, n1+n2))
        elif esc == 2:
            print('Opção MULTIPLICAR escolhida:')
            print('{} x {} = {}'.format(n1, n2, n1*n2))
        elif esc == 3:
            print('Opção MAIOR escolhida:')
            if n1 > n2:
                maior = n1
            elif n2 > n1:
                maior = n2
            else:
                print('Os valores são iguais')
            print('{} é o maior'.format(maior))
        elif esc == 4:
            print('Opção inserir novos valores:')
            n1 = int(input('Digite um primeiro novo valor: '))
            n2 = int(input('Digite um segundo novo valor: '))
        elif esc == 5:
            aceito = True
    print('=' * 30)
    sleep(2)
print('Fim do programa, volte sempre!')