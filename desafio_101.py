def voto(ano=0):
    print('-' * 25)
    from datetime import datetime
    atual = datetime.now().year - ano
    if atual < 16:
        print(f'{atual} anos: VOTO NEGADO.')
    elif 18 <= atual < 65:
        print(f'{atual} anos: VOTO OBRIGATÓRIO.')
    else:
        print(f'{atual} anos: VOTO OPCIONAL.')


# Pp
voto(int(input('Ano de nascimento: ')))