# Напишите программу, которая принимает на 
# вход вещественное число и показывает сумму его цифр.
number = (input('Введите вещественное число:'))
summ = 0
for digit in number:
    if digit.isdigit():
        summ += int(digit)
print(f'Сумма цифр в цисле равна: {summ}')