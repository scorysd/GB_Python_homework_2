# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число
n = int(input('Введите число:'))
my_list = []
for i in range(-n,n+1):
    my_list.append(i)
print(my_list)
file = open("file.txt", "r")
index = file.read()
index = list(index)
result = 1
new_index = []
for i in index:
    if i.isdigit(): 
        a = int(i)
        new_index.append(i)
        result *= (my_list[a])
print(f'Произведение элементов на позициях {new_index} равно: {result}')
