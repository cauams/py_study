# Generator Expressions

from sys import getsizeof

numeros = [x * 10 for x in range(10000000)]

print(f'LIST: Tipo: {type(numeros)}, Tamanho: {getsizeof(numeros)}')

print()

numeros = (x * 10 for x in range(100000000))

print(f'GENERATOR: Tipo: {type(numeros)}, Tamanho: {getsizeof(numeros)}')
