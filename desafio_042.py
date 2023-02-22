#Triangulo 2.0. Este código verifica se um triangulo pode existir e qual é o seu tipo
print('\033[7m Veremos se as medias inseridas podem criar um triângulo e de qual tipo \033[m')
a = float(input('Digite a primeira medida: '))
b = float(input('Digite a segunda medida: '))
c = float(input('Digite a terceira medida: '))
if a < b + c and b < a + c and c < a + b:
    print('\033[34mCom as medidas {:.1f}, {:.1f}, {:.1f} um triângulo pode ser construido\033[m'.format(a, b, c))
    if a == b == c:
        forma = 'EQUILÁTERO'
    elif a == b or b == c or c == a:
        forma = 'ISÓSCELES'
    else:
        forma = 'ESCALENO'
    print('O triângulo é do tipo {}'.format(forma))
else:
    print('\033[31mCom as medidas inseridas um triângulo NÃO pode ser construido\033[m')
