#Programa que recebe um valor e apresenta seu sucessor e anecessor de duas formas
n = int(input('Digite um número: '))
ns = n + 1 #Apresentação do valor sucessor e antecedor através da criação de variaveis para cada um
na = n - 1
print('O número digitado é {}, seu sucessor é {} e seu antecessor é {}'.format(n, ns, na))
print('O número digitado é {}, seu sucessor é {} e seu antecessor é {}'.format(n, (n+1), (n-1))) #Apresentação do valode sucessor e antecedor através de soma e subtração na própria impressão dos dados
