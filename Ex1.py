# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

n = int(input('Введите число: '))
asd = 0
while(n>0):
    dig = n%10
    asd = asd+dig
    n = n//10
print("\033[H\033[J")
print('Сумма цифр в числе = ', asd)