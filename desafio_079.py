#Este código gera uma tabela de tamanho indefinido até que o usuário não queira mais
valores = []
while True:
    n = int(input('\nDigite um valore: '))
    if n in valores:
        print(f'O valor {n} já existe. \nNão armazenado...')
    else:
        valores.append(n)
        print('Armazenado com sucesso...')

    x = input('Quer inserir outro número? [Y/N] \n:')
    if x in 'Nn':
        break
valores.sort()
print(f'O números inseridos foram {valores}')
