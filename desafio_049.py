#Refazendo o desafio 009, forma mais eficiente de construção de tabela de vezes
x = int(input('Digite qual tabuada gostaria de ver: '))
print('-' * 12)
for tab in range(0, 11, 1):
    print('{} X {:2} = {}'.format(x, tab, x * tab))
print('-' * 12)