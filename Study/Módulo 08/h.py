# Sets
    # Evita itens duplicados
    # Não possui Index

lista1 = [10, 20, 30, 40, 50, 70, 90, 120]
lista2 = [10, 20, 40, 60, 100, 123]

set1 = set(lista1)
set2 = set(lista2)

print(set1 | set2) # Union
print(set1 - set2) # Difference
print(set1 ^ set2) # Symmetric Difference
print(set1 & set2) # And

print()

# Sintax direta para a formação de um set + aglumas funções:

set3 = {1, 2, 3, 4, 5}
set3.add(6)
set3.update([7, 8, 9, 10])
set3.remove(10) # Apresenta erro caso queira remover algo que não exista dentro do set
set3.discard(9) # Não apresenta erro caso queira remover algo que não exista dentro do set

print(type(set3))
print(set3)