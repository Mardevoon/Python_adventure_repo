#Este código joga dados aleatóriamente de 4 jogadores e depois organiza os vencedores por posição
from random import randint
from time import sleep
from operator import itemgetter
#Código do professor
jogo = {'jogador 1': randint(1, 6),
        'jogador 2': randint(1, 6),
        'jogador 3': randint(1, 6),
        'jogador 4': randint(1, 6)}
ranking = dict()
print('Valores sorteados:')
for k, v in jogo.items():
    print(f'O {k} tirou {v} no dado.')
    sleep(0.1)
print('-=' * 30)
print('Ranking dos jogadores:')
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'{i+1}° lugar: {v[0]} com {v[1]}.')
    sleep(0.1)