#Esté código ler o número e diz se ele é primo

n = int(input('Digite um número para que eu possa adivinhar se ele é primo ou não:'))

print('O número {} é divisível por:'.format(n))
t = 0
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[36m', end = ' ')
        t += 1
    else:
        print('\033[m', end = ' ')
    print('{}'.format(c), end= ' ')
print('\n\033[mO número {} foi dividido {} vezes'.format(n, t))
if t == 2:
    print('\033[mPortanto ele é primo')
else:
    print('\033[mPortanto ele não é primo')