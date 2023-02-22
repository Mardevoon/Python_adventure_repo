#Este código se apresenta ao usuário e diz qual é o seu primeiro nome e seu último
nome = str(input('Digite seu nome completo: ')).strip()
sepa = nome.split()
print('É uma estranha sensação lhe conhecer!')
print('Seu primeiro nome é {}'.format(sepa[0]))
print('Seu último nome é {}'.format(sepa[len(sepa)-1]))
