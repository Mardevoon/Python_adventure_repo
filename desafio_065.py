#Este código tira a média d edois valores e mostra qual foi o maior e menor valor inserido
esc = 'S'
y = x = cont = soma = 0
while esc != 'N':
    n = int(input('Digite um número: '))
    soma += n
    cont +=1
    if cont == 1:
        x = y = n
    else:
        if n > x:
            x = n
        if n < y:
            y = n
    esc = str(input('Gostaria de continuar? ')).upper().strip()
print('A média dos {} números é {}'.format(cont, (soma / cont)))
print('O maior número foi {}'.format(x))
print('O menor número foi {}'.format(y))