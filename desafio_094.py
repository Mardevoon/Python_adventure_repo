#Este código faz um processamento de dados
pessoa = dict()
dados = list()
med = 0

#ENTRADA DE DADOS
while True:
    pessoa['nome'] = str(input('Nome: '))
    while True: #Laço de segurança do sexo
        pessoa['sexo'] = str(input('Sexo [M/F]: ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        else:
            print('ENTRADA INVÁLIDA! Digite somente M ou F')
    while True: #Laço de segurança da idade
        pessoa['idade'] = int(input('Idade: '))
        if pessoa['idade'] >= 0:
            break
        else:
            print('ENTRADA INVÁLIDA! Digite somente um valor positivo')
    dados.append(pessoa.copy()) #Cópia os dados do dicionario na lista
    while True: #Laço de segurança da saída do loop
        resp = str(input('Inserir outra pessoa? [S/N]: ')).upper()[0]
        if resp not in 'SN':
            print('ENTRADA INVÁLIDA! Digite somente S ou N')
        else:
            break
    if resp in 'N':
        break
    print() #Caso a escolha de resp seja "s" irá dá um espaço para reiniciar o programa
#FIM DA ENTRADA DE DADOS

#PROCESSAMENTO DOS DADOS
print('=' * 60)
for m in range(0, len(dados)):  #Laço para somar todas as idade e depois descobrir a média
    med += dados[m]['idade']
med /= len(dados)
print(f'A) No total, {len(dados)} pessoas foram cadastradas.')
print(f'B) A média de idade é {med:.2f} anos.')
print('C) As mulheres cadastradas foram ', end='')
for w in dados: #Laço para pegar todas as mulheres cadastradas
    if w['sexo'] in 'Ff':
        print(w['nome'], end='... ')
print('\nD) Lista de pessoas com idade acima da média:')
for am in dados:    #Laço para pegar todas as pessoas com idade acima da média
    if am['idade'] >= med:
        print('     ', end='')
        for k, v in am.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<< ENCERRANDO >>')
#FIM DO PROCESSAMENTO DOS DADOS