contatos = []

for i in range(3):
    print(f'\nContato {i+1}')
    con = {}

    con['nome completo'] = input('Informe seu nome completo: ')
    con['telefone'] = int(input('Informe seu telefone: '))
    con['e-mail'] = input('Informe seu e-mail: ')
    contatos.append(con)

for con in contatos:
    print(f'\nNome: {con['nome completo']}')
    print(f'Telefone: {con['telefone']}')
    print(f'E-mail: {con['e-mail']}')