#Este código determina quanto de aumento o funcionário receberá
sal = float(input('Digite o seu salário:'))
if sal > 1250:
    novo = 10 * sal / 100 + sal
else:
    novo = 15 * sal / 100 + sal
print('O seu salário de R${} passará a ser R${}'.format(sal, novo))
