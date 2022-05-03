# Написать программу, которая удаляет первый и последний символы строки.
# Если строка содержит меньше  двух символов - вывести сообщение об ошибке.

String = input('Write string: ')

if len(String)>2:
    String = String[1:-1]
    print(String)
if len(String)==2:
    String = None
    print(String)
else:
    print('Строка содержит менее двух символов!')

