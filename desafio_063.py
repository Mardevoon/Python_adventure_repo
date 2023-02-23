#Este código cria uma Sequência de Fibonacci a ártir de um valor inserido


print('-' * 23)
print('Sequência de Fibonacci')
print('-' * 23)

n = int(input('Insira quantos termos gostaria de ver: '))

t0 = 0
t1 = 1
print('{} → {}'.format(t0, t1), end='')

cont = 3
while cont <= n:
    t3 = t0 + t1
    print(' → {}'.format(t3), end='')
    t0 = t1
    t1 = t3
    cont += 1
print(' → FIM')