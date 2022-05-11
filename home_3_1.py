#Вы вводите с клавиатуры 2 числа (например 2 и 12),
# вам нужно написать программу, которая выведет количество чисел в данном промежутке не кратных 5.

while True:
    try:
        first_number = int(input('Введите начальное(целое) число: '))
        break
    except ValueError:
        print('Вы должны ввести именно целое число!')
while True:
    try:
        last_number = int(input('Введите конечное(целое) число: '))
        break
    except ValueError:
        print('Вы должны ввести именно целое число!')

list_number =list(i for i in range(first_number,last_number +1))
for item in list_number:
    if item%5!=0:
        print(item)