# Напишите программу, которая принимает на вход число N
# и выдает набор произведений чисел от 1 до N.
def mult(n):
    count = 1
    result = 1
    while  count <= n:
        result = count * result
        print(result, end=" ")
        count += 1
n = int(input('Введите число:'))
mult(n)