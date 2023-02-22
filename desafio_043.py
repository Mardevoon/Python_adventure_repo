#Este código cálcula o IMC de uma pessoa
print('CÁLCULAR IMC (Indice de Massa Corporal)')
peso = float(input('Insira seu peso (Kg): '))
altura = float(input('Insira sua altura em metros (m): '))
IMC = peso / altura ** 2
if IMC <= 18.5:
    situacao = 'ABAIXO DO PESO NORMAL'
elif IMC <= 25:
    situacao = 'NO PESO IDEAL'
elif IMC <= 30:
    situacao = 'COM SOBREPESO'
elif IMC <= 40:
    situacao = 'EM OBESIDADE, CUIDADO'
else:
    situacao = 'EM OBESIDADE MÓRBIDA! VÁ PARA O HOSPITAL!'
print('Seu IMC é {:.1f}, você está {}'.format(IMC, situacao))
