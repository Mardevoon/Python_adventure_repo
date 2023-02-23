#Este código Armazena o nome de alunos, suas notas, média e se ele(a) passou
dados = dict()
dados['nome'] = str(input('Nome: '))
dados['media'] = float(input(f'Média de {dados["nome"]}: '))
if dados['media'] >= 7:
    dados['situacao'] = 'Aprovado'
elif 5 <= dados['media']:
    dados['situacao'] = 'Recuperação'
else:
    dados['situacao'] = 'Reprovado'
print(f'Nome é igual a {dados["nome"]}')
print(f'Média é igual a {dados["media"]}')
print(f'Situação é igual a {dados["situacao"]}')