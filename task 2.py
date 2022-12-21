# Дан список, вывести отдельно буквы и цифры, пользуясь filter.
# [12,'sadf',5643] ---> ['sadf'] ,[12,5643]

import os
os.system('cls')

print('Задача № 2')

bools = ['12', 'sadf', '5643', 'vvbds']

out = filter(None, bools)

for iter in out:
    print(iter)



# print('Список уникальных элементов: ', list )