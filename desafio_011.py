#Programa que cálcula o quanto de tinta será necesssário para pintar uma determinada área de parede
alt = float(input('Altura da parede em metros: '))
lag = float(input('Largura da parede em metros: '))
area = lag*alt
tinta = area/2
#um litro de tinta pinta 2 m2
print('As dimensões de {} metros de altura e {} de largura tem uma área de {:.2f} metros quadrados. \n Você '
      'precisará de {:.2f}L de tinta'.format(alt, lag, area, tinta))
