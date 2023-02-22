#Código que convete a moeda real para dolar, euro e yen
real = float(input('Converdor de real: R$'))
#11/07/2021 US$5.20
#11/07/2021 EU$6.18
#11/07/2021 ¥0.0047
print('Com {:.2f} você tem as seguintes quantidades nestas moedas: \n US${:.2f} \n EU${:.2f} \n ¥{:.2f}'.format(real, (real/5.20), (real/6.18), (real/0.047)))
