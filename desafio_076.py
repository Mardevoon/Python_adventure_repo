#Este código cria uma tabela de preços
produto = ("Refrigerante", 7.99,
           "Caneta ponta pincél", 39.99,
           "Borracha", 2,
           "Apontador eletrico", 49.99,
           "Lápis de colorir", 12.99)
print('-' * 40 )
print(f'{"TABELA DE VALORES":^40}')
print('-' * 40 )
for p in range(len(produto)):
    if p % 2 ==0:
        print(f'{produto[p]:.<32}',end='')
    else:
        print(f'R$ {produto[p]:>5.2f}')
print('-' * 40 )

