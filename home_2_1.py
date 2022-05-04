#Вы вводите с клавиатуры последовательность чисел, разделённых запятой.
#Составьте список и кортеж с этими числами.
# один из вариантов решения


input_string = input("write number: ")
input_string_in_list = input_string.split(",")



input_string_in_tuple = tuple(input_string_in_list)

print(input_string_in_list, type(input_string_in_list))
print(input_string_in_tuple,type(input_string_in_tuple))