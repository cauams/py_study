# Função LAMBDA:
    # Não tem nome.
    # Pode conter varios args, mas só pode ter ume expressão.
    # Código mais claro.
    # Costuma ser ultilizada dentro de outras funções

def calc(x):
    soma = lambda x: x + 10
    return soma(x) * 4

print(calc(2))