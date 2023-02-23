#Este código pega o nome de um jogador, quantas partidas jogou e a quantidade de gols feitos em cada uma
dados = dict()
jogos = list()
dados['nome'] = str(input('Nome do jogador: '))
dados['partidas'] = int(input(f'Quantas partidas {dados["nome"]} jogou? '))
for p in range(0, dados['partidas']):
     jogos.append(int(input(f'    Quantidade de gols na {p+1}° partida: ')))
dados['gols'] = jogos[:]
dados['total'] = sum(jogos)
print('=' * 60)
print(dados)
print('=' * 60)
for k, v in dados.items():
    print(f'A campo {k} tem o valor {v}')
print('=' * 60)
print(f'O jogador {dados["nome"]} jogou {dados["partidas"]} partidas.')
for p, v in enumerate(dados['gols']):
    print(f'    => Nas {p+1}° partida, fez {v} gols.')
print(f'Foi um total de {dados["total"]} gols.')