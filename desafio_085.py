#Ente código separa os valores em pares e impares
num = []
par = []
imp = []
for c in range(0, 7):
    n = int(input(f'Digite o {c+1}° valor: '))
    if n % 2 == 0:   par.append(n)
    else:   imp.append(n)
par.sort()
imp.sort()
num.append(par[:])
num.append(imp[:])
print('=-'*30)
print(f'Os valores pares inseridos foram {num[0]}')
print(f'Os valores ímpares inseridos foram {num[1]}')