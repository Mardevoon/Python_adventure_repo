#Este código cria uma lista com diversos valores e os organiza de forma descrescente
valores = []
while True:
    valores.append(int(input('\nDigite um valor: ')))
    x = input('Adicionar outro valor? [Y/N]\n: ')
    if x in 'Nn': break

print('=-' * 30)
valores.sort(reverse=True)
print(f'\nVocê digitou {len(valores)} elementos')
print(f'Valores ordenados em forma decrescente {valores}')
if 5 in valores: print('O valor 5 esta na lista!')
else: print('O valor 5 não esta na lista!')