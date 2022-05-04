#Напишите проверку на то, является ли строка палиндромом.

String = input('Write string: ')
if String == ''.join(reversed(String)):
    print('Строка полиндром')
else:
    print('Строка не полиндром')