# Написать программу, которая удаляет первый и последний символы строки.
# Если строка содержит меньше  двух символов - вывести сообщение об ошибке.

while True:
    string = input('Введите строку и мы удалим первый и последний символы: ')
    if len(string)>2:
        string = string[1:-1]
        print(string, ' - Ваша строка после удаления символов.')
        break
    elif len(string)==2:
        string = " "
        print(string, ' - Вы ввели два символа, после удаления строка пуста.')
        break
    else:
        print('Строка содержит менее двух символов!')

