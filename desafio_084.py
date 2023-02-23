'''Este código recebe dados de várias pessoas, diz quantas
 pessoas foram inseridas e qual foi o maior e menor valor inserido'''
dados = []
aux = []
tot = 0
while True:
    aux.append(str(input('Nome: ')))
    aux.append(int(input('Peso: ')))
    dados.append(aux[:])
    aux.clear()
    if tot == 0:
        mai = men = dados[0][1]
    else:
        if dados[tot][1] > mai:
            mai = dados[tot][1]
        if dados[tot][1] < men:
            men = dados[tot][1]
    tot += 1
    resp = str(input('Continuar? [S/N] : '))
    if resp in 'Nn': break
print('=-' * 30)
print(f'Ao total {tot} pessoas foram cadastradas.')
print(f'O maior peso inserido foi de {mai}Kg. Pertencente a ', end='')
for c in range(0, tot):
    if mai == dados[c][1]: print(dados[c][0], end='.. ')
print(f'\nO menor peso inserido foi de {men}Kg. Pertencente a ', end='')
for c in range(0, tot):
    if men == dados[c][1]: print(dados[c][0], end='.. ')