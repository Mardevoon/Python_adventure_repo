#Este código armazena valores nas posições e faz a soma deles em certas posições
vet = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
s = sc = 0
for l in range(0, 3):
    for c in range(0, 3):
        vet[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('='*60)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{vet[l][c]:^5}]', end='')
        if vet[l][c] % 2 == 0:
            s += vet[l][c]
    sc += vet[l][2]
    print()
print('=' * 60)
print(f'A soma de todos os números pares é {s}.')
print(f'A soma de todos os números da terceira coluna é {sc}.')
print(f'O maior valor da segunda linha foi {max(vet[1])}.')