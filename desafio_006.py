#Programa que mostra o dobro, triplo e raíz d eum valor inserido
n = int(input('Digite um número: '))
nd = n * 2
nt = n * 3
nr = n ** (1/2)
print('O digito primario é {}, o dobro dele é {}, o triplo é {} e a raíz é {:.2f}'.format(n, nd, nt, nr))
#opção menor
print('O digito primario é {}, o dobro dele é {}, o triplo é {} e a raíz é {:.2f}'.format(n, (n*2), (n*3), (n ** (1/2))))
