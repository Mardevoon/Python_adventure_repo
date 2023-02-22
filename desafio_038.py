# Este código verifica se os númeors são maiores, menores ou iguais
a = int(input('Digite um número: '))
b = int(input('Digite outro número: '))
if b > a:
    maior = b
    print('O segundo valor é o MAIOR')
elif a > b:
    maior = a
    print('O primeiro valor é MAIOR')
else:
    print('Os números são IGUAIS')
