#Напишите программу, которая проверяет является ли число четным.

while True:
    try:
        number = int(input('Введите Целое число: '))
        break
    except ValueError as ex:
        print('Введите число!!!',ex)

if number%2==0:
    print('Ваше число четное.')
else:
    print('Ваше число не четное.')
