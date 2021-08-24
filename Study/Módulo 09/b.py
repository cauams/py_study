# Erro

from typing import ValuesView


try:
    idade = int(input('Digite a sua idade: '))
    print(idade)
except ValueError:
    print('Por favor digite um número!')
