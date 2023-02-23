'''Este código ler o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.'''
i = 0
iM = 0
nM = ''
iF = 0
for c in range (1, 5):
    print('-----{} PESSOA-----'.format(c))
    nome = str(input('Digite o nome: ')).upper()
    idade = int(input('Digite a idade: '))
    sexo = str(input('sexo [M/F]: ')).upper()

    if c == 1 and sexo == 'M':
        nM = nome
        iM = idade
    if idade > iM:
        nM = nome
        iM = idade
    else:
        if idade < 20:
            iF += 1

    i += idade
print('A idade média do grupo é {} anos'.format(i / 4))
print('O homem mais velho é {}, com {} anos'.format(nM, iM))
print('Ao todo são(é) {} mulher(es) com menos de 20 anos'.format(iF))