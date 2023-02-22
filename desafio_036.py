#Este programa faz o financiamento de uma casa
casa = float(input('Valor da casa: R$'))
salaria = float(input('Diga seu salário: R$'))
ano = int(input('Quantos anos de financiamento: '))
print('CÁLCULANDO...')
financiamento = casa / (ano * 12)
if salaria * 30 / 100 <= financiamento:
    print('\033[31mO SEU EMPRÉSTIMO FOI NEGADO!\033[m')
    print('O seu salário é insuficiente para fazer o empréstimo da casa')
else:
    print('\033[34mO SEU EMPRÉSTIMO FOI ACEITO!\033[m')
    print('Seu financiamento será de R${:.2f} ao mês'.format(financiamento))
