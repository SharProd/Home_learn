#Напишите проверку на то, является ли строка палиндромом.

string = input('Write string: ')
if string == string[::-1] :
    print('Строка полиндром')
else:
    print('Строка не полиндром')