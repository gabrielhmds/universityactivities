# Cadastro de alunos
alunos = ['João', 'Maria', 'Pedro']

# Cadastro de usuários
usuarios = {'user': '123'}

# Autenticação por senha
tentativas = 0
while True:
    user = input('Usuário: ')
    senha = input('Senha: ')

    if usuarios.get(user) == senha:
        print('Acesso permitido')
        break
    else:
        tentativas += 1
        if tentativas == 3:
            print('Acesso bloqueado')
            break
        print('Usuário ou senha incorretos. Tentativas restantes: ' + str(3 - tentativas))

# Inserção das notas
if tentativas < 3:
    for aluno in alunos:
        print('Digite as notas de ' + aluno)
        nota1 = float(input('Nota 1: '))
        nota2 = float(input('Nota 2: '))
        media = (nota1 + nota2) / 2
        print('Média de ' + aluno + ': ' + str(media))