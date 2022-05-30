#Написать программу, которая просит ввести номер карточки и после успешного введения номера,
# маскирует все символы кроме последних четырех.
# Нужно добавить проверку на введенный номер. (не должно быть букв и количество цифр должно = 16)

while True:
    try:
        number = int(input('Введите шестьнадцатизначное число: '))
        number = str(number)
        if len(number)==16:
            break
        if len(number) != 16:
            print('Введите число длинной в 16 символов!')
    except ValueError:
        print('Вы должны ввести целые число!')

number_secure = ("*"*12)+number[-4:len(number)]
print(number_secure)

while True:
    try:
        number_2 = int(input('Введите число еще раз: '))
        number_2 = str(number_2)
        if len(number)==16:
            break
        if len(number_2) != 16:
            print('Введите число длинной в 16 символов!')
    except ValueError:
        print('Вы должны ввести целые число!')

if number == number_2:
    print('Все верно, ваши числа равны!')
else:
    print('Ошибка, числа не равны!')