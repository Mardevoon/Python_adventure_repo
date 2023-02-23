'''Este código utiliza uma tupla preenchida com os 20 primeiros colocados da Tabela do
    Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:'''

colocados = ('ATRLÉTICO', 'FLAMENGO', 'PALMEIRAS', 'FORTALEZA', 'CORINTHIANS', 'BRAGANTINO', 'FLUMINENSE', 'AMÉRICA',\
            'ATLÉTICO', 'SANTOS', 'CEARÁ', 'INTERNACIONAL', 'SÃO PAULO', 'ATHLETICO', 'CUIABÁ', 'JUVENTUDE', 'GRÊMIO',\
            'BAHIA', 'SPORT', 'CHAPECOENSE')
print(f'Os primeiros 5 times do Brasileirão são: {colocados[0:5]}')
print('=-' * 55)
print(f'OS últimos 4 times do Brasileirão são: {colocados[-4:]}')
print('=-' * 55)
print(f'Os times do Brasileirão em ordem alfabética são: {sorted(colocados)}')
print('=-' * 55)
print(f'O time Chapecoense está na posição {colocados.index("CHAPECOENSE") + 1}')