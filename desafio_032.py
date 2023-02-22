#Este código verifica se o ano inserido é bissexto
from datetime import date
print('O ano é BISSEXTO?')
ano = int(input('Digite algum ano ou digite 0 para analizar o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 >= 1 and ano % 100 >= 1 or ano % 400 >= 1:
    print('O ano de {} NÃO é bissexto'.format(ano))
else:
    print('O ano de {} É bissexto'.format(ano))
print('-----FIM-----')
