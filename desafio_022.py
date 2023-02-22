#O código recebe o nome de uma pessoa e faz várias coisas
nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando nome...')
print('Seu nome em maiúsculo é {}'.format(nome.upper()))
print('Seu nome em minúsculo é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))

    #Opeção um para contar o primeiro nome
#print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))

    #Opção dois para contar o primeiro nome
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))
print('Seu nome do meio é {} e ele tem {} letras'.format(separa[1], len(separa[1])))