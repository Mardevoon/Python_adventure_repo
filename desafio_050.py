#Este código ler seis valores inteiros e mostre a soma daqueles que forem pares
soma = 0
for c in range(1, 7, 1):
    n = int(input("Digite qualquer número, irei soma somente dos que forem pares: "))
    if n % 2 == 0:
        soma += n
print('A soma de todos os números pares é: {}'.format(soma))