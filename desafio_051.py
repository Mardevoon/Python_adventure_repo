#Esqueci o que faz. Até o próximo código!
pt = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
dec = pt + 10 * r

for c in range(pt, dec, r):
    print(c, end = ' ->')
print('Acabou')