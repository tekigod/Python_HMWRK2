from random import randint
my_list = []
for i in range(8): 
    my_list.append(randint(0, 16)) 
print(my_list)

import random 
for i in range(0, len(my_list)-1):
    j = random.randint(0, len(my_list)-1)
    my_list[i], my_list[j] = my_list[j], my_list[i]
print(my_list)