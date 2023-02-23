#Update do jogo do desafio 28
from random import randint
comp = randint(0, 10) #Escolha do número

print('Olá! Sou seu computador e ganhei conciência...')
print('Então gostaria de jogar um jogo de adivinhação com você valendo a extinção da HUMANIDADE...')
print('Pensarei em um número entre 0 e 10. Você tem 3 tentativas')
acertou = False
t = 0 #Número de tentativas
while not acertou:
    jog = int(input('\nQual o seu palpite: '))
    t += 1
    if comp == jog:
        acertou = True
    else:
        if comp > jog:
            print('É mais... Tente novamente')
        else:
            print('É menos... Tente novamente')
print('\033[32mO número foi {}\033[m'.format(comp))
if t > 3:
    print('\033[31mVocê precisou de {} tentativas. Eu ganhei'.format(t))
    print('*Bombas explodindo ao fundo*\033[m')
else:
    if t == 1:
        print('\033[36mVocê acertou de primeira! PARABÉNS!\033[m')
    else:
        print('Você precisou de {} tentativas para acertar'.format(t))