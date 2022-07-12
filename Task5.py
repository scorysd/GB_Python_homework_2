# Реализуйте алгоритм перемешивания списка
import random
n = int(input('Введите число:'))
my_list = []
for i in range(-n,n+1):
    my_list.append(i)
print(my_list)
random.shuffle(my_list)
print(my_list)
