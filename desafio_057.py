#Este código ler o sexo de uma pessoa, mas somente aceita valores ‘M’ ou ‘F’.
sexo = str(input('Insira o sexo do ser vivo [F/M]: ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Sexo fora da base de dados. Por favor, informe o sexo: ')).strip().upper()[0]
print('Sexo {} registrado'.format(sexo))