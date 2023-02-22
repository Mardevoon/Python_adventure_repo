#Este código ler o nome de uma cidade e diz se ela começa ou não com o nome “SANTO”.

"""cid = str(input('Digite o nome de uma cidade: ')).strip()
m = cid.upper()
print('A cidade escolhida começa com "SANTO"? {}'.format(cid, 'SANTO' in m))"""""

cid = str(input('Digite o nome de uma cidade: ')).strip().upper()
sep = cid.split()
print('A cidade tem "SANTO" no nome? {}'.format('SANTO' in cid))
print('O nome da cidade escolhida começa com "SANTO"? {}'.format('SANTO' in sep[0]))