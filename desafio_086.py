#Este código armazena valores na posições descritas na impressão
vet = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for c in range(0, 3):
    for v in range(0, 3):
        vet[c][v] = int(input(f'Digite um valor para [{c}, {v}]: '))
print('='*30)
for c in range(0, 3):
    for v in range(0, 3):
        print(f'[{vet[c][v]:^5}]', end='')
    print()