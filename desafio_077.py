#Este código diz quais palavras na memória tem 'aeiou' e quantas vocais tem cada palavra
palavras = ('Trecho', 'Diariamente', 'Molar', 'Plural', 'Assassinato', 'Champanhe', 'Fondue', 'Engrenagem',
            'Muleteiro', 'Beco', 'oBoticario')

for word in palavras:
    cont = 0
    print(f'Na palavra {word} temos: ', end='')
    for letra in word:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
            cont += 1
    print(f'\nUm total de {cont} vocais')
    print('-' * 40)
    cont = 0