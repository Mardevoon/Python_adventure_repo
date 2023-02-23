def fatorial(n, show=False):
    """
    -> Calcula o Fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor final do Fatorial.
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(f' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


# Pp
valor = int(input('Digite um valor: '))
pro = str(input('Mostrar processo? [S|N]: '))
if pro in 'Ss':
    print(fatorial(valor, show=True))
else:
    print(fatorial(valor))