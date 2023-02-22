#Para vencer este jogo você precisa adivinhar o número que o computador esta pensando
from random import choice
from time import sleep
print("Vamos joar um jogo! \nVocê tem que adivinhar o número que estou pensando")
print('\033[33m - \033[m' * 21)
r = int(input('Escolha um número de 0 a 5: '))
lista = [0, 1, 2, 3, 4, 5]
esc = choice(lista)
print("PROCESSANDO")
sleep(1)
print(".")
sleep(1)
print(".")
sleep(1)
print(".")
sleep(1)
print('O número escolhido pelo pc foi {}'.format(esc))
if r == esc:
    print('\033[32m VOCÊ VENCEU! \033[m')
else:
    print('\033[31m VOCÊ PERDEU! \033[m')
print('\033[33m ---------Fim--------- \033[m')