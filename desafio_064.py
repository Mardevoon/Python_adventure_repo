#Este código ler vários números inteiros para somar, digidando 999 para encerrar
cont = r = n = 0
while n != 999:
    n = int(input('Digite um número (999 para parar): '))
    if n != 999:
        r = r + n
        cont += 1
if cont == 0:
    print('Você não digitou nenhum número')
else:
    print('Você digitou {} números, a soma de todos é {}'.format(cont, r))