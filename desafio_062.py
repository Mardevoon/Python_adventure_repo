#Atualização do desafio 061
print('GERADOR DE PA 2.0')
print('=' * 20)
pa = int(input('Primeiro Termo: '))
r = int(input('Razão da PA: '))
c = 0
t = 10
while c != t:
    print('{}'.format(pa), end='')
    print(' → ' if c < t-1 else ' → FIM', end='')
    pa += r
    c += 1
    if c == t:
        mt = int(input('\n\nQuantos termos gostaria de mostrar a mais? '))
        if mt == 0:
            print('FIM DO GERADOR com {} termos exibidos'.format(t))
        else:
            t += mt
