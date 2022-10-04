# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

n = int(input('Введите число: '))
def n_list(n):
    list=[]
    for i in range(-n, n+1):
        list.append(i)
    return list

print(n_list(n))

scroll = n_list(n)
i1 = int(input('Введите позицию 1ого элемента: '))
i2 = int(input('Введите позицию 2ого элемента: '))
for i in range(-n, n+1):
    mult = scroll[i1] * scroll[i2]
print(f'Произведение элементов c индексами {i1} и {i2} = {mult}')