# Map Function

list0 = [1, 2, 3 , 4]

def multi(x):
    return x * 2

list1 = map(multi, list0)
list2 = list(map(multi, list0))


print(list1)
print(list2)

print()

# Map function com lambda

print(map(lambda x: x * 10, list0))
print(list(map(lambda x: x * 10, list0)))