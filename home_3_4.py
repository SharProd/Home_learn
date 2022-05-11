#Написать проверку на то, является ли введенное число нарциссическим:
# Пример 153 = 1^3 + 5^3 + 3^3. 153 - число нарцисс (число в степени - длина числе)
while True:
    try:
        number = int(input('Введите число: '))
        break
    except ValueError:
        print('Вы ввели не число!')

list_number = list(str(number))
result_number = 0

for i in list_number:
    i = int(i)
    result_number+=i** (len(list_number))

if number == result_number:
    print('Ваше число нарцисс!')
else:
    print('Вваше число не нарцисс!')
    for i in range(number-(number//2),number+200):
        list_number = list(str(i))
        result_number_else = 0
        for item in list_number:
            item = int(item)
            result_number_else += item ** (len(list_number))
            if i == result_number_else:
                print('Ближайшие числа нарцисс - ',result_number_else)



