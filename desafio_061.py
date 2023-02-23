#Este código gera uma PA
print('GERADOR DE PA')
print('=' * 18)
pa = int(input('Primeiro Termo: '))
r = int(input('Razão da PA: '))
c = 0
while c != 10:
    print('{}'.format(pa), end='')
    print(' → ' if c < 9 else ' → FIM', end='')
    pa += r
    c += 1