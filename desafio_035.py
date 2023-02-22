#Este código determina, a partir das medidas inseridas, se um triangulo pode existir
'''a < b + c
   b < a + c
   c < a + b'''
from time import sleep
print('Vamos criar um triângulo!')
print('\033[31m ~^~ \033[m' * 10)
a = float(input('Digite o primeiro segmento: '))
b = float(input('Digite o segundo segmento: '))
c = float(input('Digite o terceiro segmento: '))
print('PROCESSANDO...')
sleep(1.5)
if a < b + c and b < a + c and c < a + b:
    print('Um triangulo PODE existir com as medidas {}, {} e {}'.format(a, b, c))
else:
    print('Um triângulo NÃO pode existir com as medidas {}, {} e {}'.format(a, b, c))
