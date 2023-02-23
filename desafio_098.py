from time import sleep
def contador(i, f, p):
    if p == 0:
        p = 1
    if p < 0:
        p *= -1
    print('-=' * 30)
    print(f'De {i} até {f}, de {p} em {p}:')
    sleep(1)
    cont = i
    if i < f:
        while cont <= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.4)
            cont += p
    else:
        while cont >= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.4)
            cont -= p
    print('FIM')


# PP
contador(1, 10, 1)
contador(10, 0, 2)
print('Sua vez!')
x = int(input('Inicial: '))
y = int(input('Fim: '))
z = int(input('Passo: '))
contador(x, y, z)
