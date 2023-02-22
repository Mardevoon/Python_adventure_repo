#Este código calcula a soma entre todos os números ímpares que são múltiplos de três e que se encontram no intervalo de 1 até 500
contagem = 0
conta = 0
for num in range(3, 501, 3):
    if num % 2 == 1:
        conta += num
        contagem += 1
print('A soma de todos os {} números ímpares múltiplos de 3 é: {}'.format(contagem, conta))

"""print('A soma dos {} números ímpares de 3 é: {}'.format(sum(range(3, 501, 6)) / 250.5, sum(range(3, 501, 6))))"""