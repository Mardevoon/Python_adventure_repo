#Este código escreve no extenso um número inserido entre 0 e 20
ext = ('zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze',\
      'Catorze', 'Quinze', 'Dezesseis ', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

while True:
      while True:
            n = int(input('Digite um número entre 0 e 20: '))
            if 0<= n <=20:
                  break
            print('Valor inserido inválido. Tente novamente')
      print(f'{n} no extenso se escreve {ext[n]}')

