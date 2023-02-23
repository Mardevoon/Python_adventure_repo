#Código número 88... Minha nossa! Não aguento maaaais!
from random import randint
from time import sleep

list = []
aux = []

print('░'*15, 'MEGA SENA', '░'*15)
c = int(input('Quantidade de jogos que deseja fazer: '))

print('°'*11, f'SORTEANDO {c} JOGOS', '°'*11)
for j in range(0, c):
    print(f'Jogo {j+1}: ', end='')
    for x in range(0, 6):
        n = randint(1, 60)  #Escolhe aleatóramente seis números entre 0 e 99
        aux.append(n)
    aux.sort()  #Organiza os valores em ordem crescente
    list.append(aux[:]) #Faz cópia dos dados do aux para list
    aux.clear() #Limpa os dados de aux

    print(f'{list[j]}\n', end='')
    sleep(1)
print('░'*15, 'BOA SORTE', '░'*15)