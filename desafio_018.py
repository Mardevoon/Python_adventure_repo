#Código que apresenta o seno, cosseno e tangente através de um ângulo inserido
from math import radians, sin, cos, tan
print('/0' * 30)
ang = int(input('Digite algum ângulo: '))

seno = sin(radians(ang))
print('O ângulo de {}° tem o SENO de: {:.3f}'.format(ang, seno))

coss = cos(radians(ang))
print('O ângulo de {}° tem o COSSENO de: {:.3f}'.format(ang, coss))

tang = tan(radians(ang))
print('O ângulo de {}° tem a TANGENTE de: {:.2f}'.format(ang, tang))
print('/0' * 30)
