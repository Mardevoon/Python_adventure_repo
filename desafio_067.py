#Este código cria tabuadas indefinidamente até a digitação de um número negativo
print('Exibidor de TABUADAS\nDigite um número NEGATIVO para PARAR')
cont = 0
while True:
    n = int(input('Qual tabuada gostaria de ver? '))
    print('-' * 35)
    if n < 0:
        break
    cont += 1
    for tab in range(0, 11, 1):
        print(f'{n} X {tab:2} = {n * tab}')
    print('-' * 35)
print(f'Foram exercutadas {cont} tabelas. Obrigada por participar')