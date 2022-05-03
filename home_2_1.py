#Вы вводите с клавиатуры последовательность чисел, разделённых запятой.
#Составьте список и кортеж с этими числами.
# один из вариантов решения

input_string = input("write number: ")
List = list()

for item in input_string:
    List.append(item)
    if item == ",":
        List.remove(item)

Tuple = tuple(List)
print(List, type(List))
print(Tuple,type(Tuple))