#Este código diz onde um número determinado apareceu
num = (int(input('Digite um valor: ')),
     int(input('Digite outro valor: ')),
     int(input('Digite outro valor: ')),
     int(input('Digite outro valor: ')))

print(f'\nOs números foram: {num}')
if 9 in num:
    print(f'\nO número NOVE apareceu {num.count(9)} vezes')
else:
    print('\nO valor NOVE não foi digitado')
if 3 in num:
    print(f'O número TRÊS está na posição {num.index(3)+1}')
else:
    print('O valor TRÊS não foi digitado')
print('Os números pares foram: ', end='')
for n in num:
    if n % 2 == 0:
        print(num, end=' ')