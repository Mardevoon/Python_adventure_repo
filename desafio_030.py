#Este código verifica se o número é par ou ímpar
n0 = int(input('Digite um número: '))
n1 = n0 % 2
if n1 == 1:
    print('O número digitado é ÍMPAR')
else:
    print('O número digitado é PAR')
print('-----FIM-----')