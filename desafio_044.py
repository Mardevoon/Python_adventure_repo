#Este código dá desconto em uma compra a partir da forma de pagamento
print('{:=^40}'.format('BEM-VINDO(A) AS LOJAS MARISCOS!'))
compra = int(input('''Por favor. Insira o valor do produtor:
---> R$'''))
pagamento = int(input('''Escolha sua forma de pagamento:
[0] Dinheiro - 10% de desconto
[1] cheque - 10% de desconto
[2] Cartão à vista - 5% de desconto
[3] Cartão 2x - Sem desconto
[4] Cartão 3x - 20% de juros
Forma de pagamento: '''))
if pagamento == 0 or pagamento == 1:
    desconto = compra - (compra * 10 / 100)
    print('Sua compra passará de R${:.2f} para R${:.2f}'.format(compra, desconto))
    print('Obrigado por sua preferencia e volte sempre!')
elif pagamento == 2:
    desconto = compra - (compra * 5 / 100)
    print('Sua compra passará de R${:.2f} para R${:.2f}'.format(compra, desconto))
    print('Obrigado por sua preferencia e volte sempre!')
elif pagamento == 3:
    print('Sua compra não terá desconto, o total a pagar é R${:.2f}'.format(compra))
    print('Obrigado por sua preferencia e volte sempre!')
elif pagamento == 4:
    juros = compra + (compra * 20 / 100)
    print('Com o juros sua compra passará de R${:.2f} para R${:.2f}'.format(compra, juros))
else:
    print('A forma de pagamento é invalida. \nTENTE NOVAMENTE')
