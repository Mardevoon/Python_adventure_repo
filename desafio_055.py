#Este código ler o peso de cinco pessoas, no final ele mostra as pessoas do maior para o menor peso
maior = 0
menor = 0
for c in range(1, 6):
    peso = float(input('Peso da {} pessoa: '.format(c)))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso inserido foi {}'.format(maior))
print('O menor peso inserido foi {}'.format(menor))