#Este código verifica quanto será cobrado em uma passagem de onibus
km = int(input('Quantos kilometros sua viajem terá: '))
if km >= 200:
    print('Sua viajem custar R$0.45 por Km, sendo assim você pagarar R${:.2f}'.format(km * 0.45))
else:
    print('Sua viagem custará R$0.50 por Km, você pagará R${:.2f}'.format(km * 0.50))
print('-----FIM-----')
