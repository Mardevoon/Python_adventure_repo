#Este código gera uma multa de carro
print('-' * 21)

multa = int(input('Digite a velocidade do carro: '))

if multa > 80:
    print('\033[31m Você ultrapassou o limite de velocidade em {} km \033[m'.format(multa - 80))
    #multa = (n1 - 80) * 7
    print('\033[31m Sua multa será de R${} \033[m'.format((multa - 80) * 7))
else:
    print('\033[32m Você está dentro do limite de velocidade \033[m')
