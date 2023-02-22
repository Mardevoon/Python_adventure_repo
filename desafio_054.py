#Este código ler a data de nascimento de sete pessoas dizendo no final quantos anos faltam para cada uma atingir a maioridade
from datetime import date

atual = date.today().year
maior = 0
menor = 0
for c in range (1, 8):
    ano = int(input(('Em que ano a {} pessoa nasceu? '.format(c))))
    data = atual - ano
    if data >= 18:
        maior += 1
    else:
        menor += 1

print('Ao todo divermos {} pessoas maiores de idade'.format(maior))
print('Ao todo divermos {} pessoas menores de idade'.format(menor))