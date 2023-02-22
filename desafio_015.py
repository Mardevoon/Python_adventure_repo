#Código qu elida com o valor a ser cobrado pelo tempo de uso de um carro
d = int(input('Por quantos dias o carro foi alugado? '))
k = int(input('Quantos kilometros foram rodados? '))
print('O total a pagar será R${:.2f}'.format(d * 60 + k * 0.15))
print('R${} de kilometros rodados'.format(k * 0.15))
print('R${} por dias alugado'.format(d * 60))