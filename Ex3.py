# Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.

def f(n): 
    result = []
    for i in range(1, n+1):
        result.append((1+1/i)**i)
    return result

n = int(input('Введите число: '))
print(f(n))

result = f(n) 
def summ_list(result):
    summ = 0
    for i in range(len(result)):
        summ += result[i]
    return summ

print(f'Cумма чисел =  {summ_list(result)}')
