#Напишите проверку на то, является ли строка палиндромом.

String = input('Write string: ')
String_reverse = ''.join(reversed(String))
if String == String_reverse:
    print('Стока полиндром')
else:
    print('Строка не полиндром')