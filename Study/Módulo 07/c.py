# Funções - Parametros DEFAULT e NON-DEFAULT

    # DEFAULT: Você define o valor no parâmetro
    # NON-DEFAULT: Você NÃO define o valor do parâmetro

def multix2(x, y=2):
    result = x * y
    print(f'O resultado da sua multiplicação é: {result}')

multix2(int(input('Seu número: ')))