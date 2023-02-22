#Este código faz um jogo de JO KEN PO
from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('{:=^40}'.format('VAMOS JOGAR JO KEN PO!'))
print('''Suas opções são:
[0] Pedra
[1] Papel
[2] Tesoura''')
jogador = int(input('Escolha sua jogogada: '))
print('\033[31mJO\033[m')
sleep(.8)
print('\033[33mKEN\033[m')
sleep(.8)
print('\033[32mPO!!!\033[m')
print('= ' * 20)
print('Jogador jogou {}'.format(itens[jogador]))
print('Computador jogou {}'.format(itens[computador]))
if computador == 0: # Computador jogou pedra
    if jogador == 0:
        print('\033[1;33EMPATE!\033[m')
    elif jogador == 1:
        print('\033[1;34mO JOGADOR VENCEU!\033[m')
    elif jogador == 2:
        print('\033[1;31mEU VENCI SEU OTÁRIO!\033[m')
    else:
        print('\033[1;32mJOGADA INVÁLIDA\033[m')
elif computador == 1: # Computador jogou papel
    if jogador == 0:
        print('\033[1;31mO COMPUTADOR VENCEU!\033[m')
    elif jogador == 1:
        print('\033[1;33EMPATE!\033[m')
    elif jogador == 2:
        print('\033[1;34mO JOGADOR VENCEU!\033[m')
    else:
        print('\033[1;32mJOGADA INVÁLIDA\033[m')
elif computador == 2: # Computador jogou tesoura
    if jogador == 0:
        print('\033[1;34mO JOGADOR VENCEU!\033[m')
    elif jogador == 1:
        print('\033[1;31mO COMPUTADOR VENCEU!\033[m')
    elif jogador == 2:
        print('\033[1;33EMPATE!\033[m')
    else:
        print('\033[1;32mJOGADA INVÁLIDA\033[m')
print('= ' * 20)
