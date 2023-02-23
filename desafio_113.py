#Função
def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mERRO: por favor, digite um número inteiro válido\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mUsuário preferiu não digitalizar esse número. \033[m')
            return 0
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mERRO: por favor, digite um número inteiro válido\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mUsuário preferiu não digitalizar esse número. \033[m')
            return 0
        else:
            return n


#Programa principal
n1 = leiaInt('Digite um número: ')
n2 = leiaFloat('Digite um número: ')
print(f'O valor inteiro digitado foi {n1} e o real foi {n2}')
