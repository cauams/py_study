# Filter function

list0 = [30, 50, 55, 60, 120, 144, 180, 200, 493]
def greaterthan60(x):
    return x > 60

# MAP FUNCTION

print(f'MAP FUNCTION: {list(map(greaterthan60, list0))}')
print(f'MAP FUNCTION W/ LAMBDA: {list(map(lambda x: x > 60, list0 ))}')

print()

# FILTER FUNCTION

print(f'FILTER FUNCTION: {list(filter(greaterthan60, list0))}')
print(f'FILTER FUNCTION W/ LAMBDA: {list(filter(greaterthan60, list0))}')


