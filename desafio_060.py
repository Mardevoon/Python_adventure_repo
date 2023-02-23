#Este código faz o fatorial de um número inserido
from math import factorial
n = int(input('Insira um valor para descobri seu fatorial: '))
f = 1
print('!{} = '.format(n), end='')
while n != 0:
    print('{}'.format(n), end='')
    print(' X ' if n > 1 else ' = ', end='')
    f = f * n
    n -= 1
print('{}'.format(f))