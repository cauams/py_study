# Erros

list = 1, 3, 4, 5, 6, 7

try:
    print(list[6])
except:
    print('Index não existe.')

# Você tambem pode especificar o erro caso saiba e pode por uma mensagem personalizada:

try:
    print(list[6])
except IndexError:
    print('Index não existe.')