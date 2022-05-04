#Вы вводите с клавиатуры последовательность чисел, разделённых запятой.
#Составьте список и кортеж с этими числами.
# один из вариантов решения

# пробовал метод split(), в данном случае он не коректно работает,
# а именно ему нужен разделитель, если его не указать( split()) получается ["строка"],
# а если указать ("") в разделителе , то выбивает ошибку. Метод хорош при разбиении по словам.

input_string = input("write number: ")
input_string_in_list = list()

for item in input_string:
    input_string_in_list.append(item)

input_string_in_tuple = tuple(input_string_in_list)

print(input_string_in_list, type(input_string_in_list))
print(input_string_in_tuple,type(input_string_in_tuple))