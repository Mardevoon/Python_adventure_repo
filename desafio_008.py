#Converte um valor em metros para cm e mm
m = float(input('Insira a medida em metros: '))
cm = m*100
mm = m*1000
print('{} metro(s) é equivalente a {:.0f} cm e {:.0f} mm'.format(m, cm, mm))
#outra opção menor
print('{} metro(s) é equivalente a {:.0f} cm e {:.0f} mm'.format(m, (m*100), (m*1000)))
