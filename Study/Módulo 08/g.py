# Tuples e Arrays

 # Tuples
    # Gastam menos memória que as LISTAS
    # Não são mutáveis (não podem ser alterados)

v_lista = ['a', 'b', 'c', 'd']
v_lista.append('e') # vai adcionar o "E" na lista

v_tuple = ('a', 'b', 'c', 'd')
# v_tuple.append('e') ## Isso não existe e não vai adcionar o "E" na lista.

print(type(v_lista))
print()
print(type(v_tuple))

    # Arrays
        # Gastam menos memória que as LISTAS
        # São mutáveis e são melhores para armazenar uma grande quantidade de dados.

from array import array

v_array = array('u', ['a', 'b', 'c', 'd']) # O "u" define que a array vai armazenar dados do tipo STR
v_array.append('e')

print(v_array)
print(v_array.itemsize)

print()

v_arrayINT = array('i', [1, 2, 3, 4]) # O "i" define que a array vai armazenar dados do tipo INT
v_arrayINT.append(5)

print(v_arrayINT)
print(v_arrayINT.itemsize)