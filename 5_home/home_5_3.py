"""Напишите программу, которая принимает два списка и выводит все элементы первого, которых нет во втором. """

first_string = input('Введите строку для создания первого списка: ') #abcd123
second_string = input('Введите строку для создания второго списка: ') #abcd

first_set_list = set(list(first_string))
second_set_list = set(list(second_string))

print(first_set_list)
print(second_set_list)
print(first_set_list-second_set_list)