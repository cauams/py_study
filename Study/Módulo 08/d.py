# Verificando itens dentro de uma lista

client_selection = input('Digite a cor que você está procurando: ')
cores = ['roxo', 'amarelo', 'vermelhor', 'verde']

if client_selection.lower() in cores:
    print('Está cor está em estoque!')
else:
    print('Esta cor não está disponivel para a compra no momento!')
