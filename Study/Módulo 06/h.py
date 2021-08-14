# For loop nested

    # outer loop
     # inner loop
     
import random
from random import randrange, uniform



for produto in range(1,6):
    print('PRODUTO '+ str(produto))
    for caracteristica in range(6):
        print(f'{caracteristica} {random.random()}')
        