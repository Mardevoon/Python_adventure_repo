#Este código cria uma lista com os valores e depois separa entre os pares e impares
com = []
par = []
imp = []
while True:
    com.append(int(input('\nDigite um valor: ')))

    x = input('Adicionar outro valor? [S/N]\n: ').upper()
    if x == 'N': break
n = len(com)
for cont in range(0, n):
    if com[cont] % 2 == 0: par.append(com[cont])
    else: imp.append(com[cont])
print(f'A lista completa é {com}')
print(f'Os números pares são {par}')
print(f'Os números impares são {imp}')