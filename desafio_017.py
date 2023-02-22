#Este código descobre a hipotenusa através de três formas diferentes
from math import sqrt
print('*Descobrir hipotenusa. Comando sqrt*')
co = float(input('Cateto oposto: '))
ca = float(input('Cateto adjacente: '))
print('A hipotenusa do c.o. {} por c.a. {} é: {:.1f}'.format(co, ca, sqrt(co**2 + ca**2)))

print('_' * 30)

print('*Sem bibliotecas*')
co = float(input('Cateto oposto: '))
ca = float(input('Cateto adjacente: '))
hip = (co**2 + ca**2) ** (1/2)
print('A hipotenusa é {:.2f}'.format(hip))

print ('_' * 30)

print('*Com biblioteca, comando hypot*')
from math import hypot
co = float(input('Cateto oposto: '))
ca = float(input('Cateto adjacente: '))
hip = hypot(co, ca)
print('A hipotenusa é {:.2f}'.format(hip))