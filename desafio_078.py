#Este código cria uma tabela com os valores inseridos
num = []
for cont in range(0, 5):
    num.append(int(input(f'Digite um valor para a posição {cont}: ')))
print('=-' * 30)
print(f'Você digitou os valores {num}')
print(f'\nO maior valor foi {max(num)} nas posições ', end='')
for c, v in enumerate(num):
    if max(num) == v: print(c, end='.. ')
print(f'\nO menor valor foi {min(num)} nas posições ', end='')
for c, v in enumerate(num):
    if min(num) == v: print(c, end='.. ')

#professor
num = []
for c in range(0, 5):
    num.append(int(input( f'Digite um valor para a posição {c}: ')))
    if c == 0:
        mai = men = num[c]
    else:
        if num[c] > mai:
            mai = num[c]
        if num[c] < men:
            men = num[c]
print('=-' * 30)
print(f'\nO maior valor foi {mai} nas posições ', end='')
for c, v in enumerate(num):
    if v == mai: print(c, end='.. ')
print(f'\nO menor valor foi {men} nas posições ', end='')
for c, v in enumerate(num):
    if v == men: print(c, end='.. ')