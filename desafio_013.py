#Código que calcular o salário com X porcento de aumento
sal = float(input('Sálario do funcionário: R$'))
#Aumento de 15%
n1 = 15*sal/100
n2 = sal+n1
print('Com aumento de 15% o salário é de R${:.2f}, um aumento de R${:.2f}'.format(n2, n1))
