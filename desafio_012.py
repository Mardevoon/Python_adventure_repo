#Código que calcular o valor de um produto com X porcento de desconto
prod = float(input('Valor do produto: R$'))
#Desconto de 5%
n1 = 5*prod/100
n2 = prod-n1
print('O valor do produto com 5% de desconto é de R${:.2f}, um desconto de R${:.2f}'.format(n2, n1))
