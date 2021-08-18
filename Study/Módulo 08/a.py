# Listas

frutas = ['abacate', 'abacaxi', 'açai', 'acerola', 'amora', 'bacaba', 'banana', 'bíriba', 'cacau', 'cajá', 'caqui']

x = input('Qual o código da sua fruta?: ')
x = int(x)

# Funções dentro de listas

frutas.append('uva')
# frutas.remove('banana')
# frutas.insert(3, 'acarajé')
# frutas.pop(0)
frutas.sort()

n = len(frutas)

while x < n:
    print(f'O código {x} representa a fruta: {frutas[x]}')
    break
else:
    print('Esse código não está registrado!')


