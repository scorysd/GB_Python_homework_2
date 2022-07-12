# Задайте список из n чисел последовательности 
# (1+1/n)^n и выведите на экран их сумму.
import math
n = int(input('Введите значение N:'))
result = 0
for n in range(1,n+1):
    print(f'При {n = } элемент = {math.pow(1+1/n, n)}')
    result += math.pow(1+1/n, n)
print(f'Сумма элементов = {result}')