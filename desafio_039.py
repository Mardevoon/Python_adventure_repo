# Este código verifica se o adolescente já pode se alistar
from datetime import date
atual = date.today().year
ano = int(input('Insira seu ano de nascimento: '))
idade = atual - ano
if idade > 18:
    passaram = idade - 18
    passaram2 = atual - passaram
    print('Você tem {} anos, seu alistamento foi a {} anos em {}'.format(idade, passaram, passaram2))
elif idade < 18:
    sera = 18 - idade
    sera2 = atual + sera
    print('Você tem {} anos, ainda faltam {} anos para fazer o alistamento, ele será em {}'.format(idade, sera, sera2))
else:
    print('Você tem 18 anos e teve fazer seu alistamento imediatamente!')
