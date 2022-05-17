"""Отсортируйте словарь по значению в порядке возрастания и убывания. """

dict_x_y = {'d' : 1, 'c' : 3, 'b' : 2 , 'a' : 4}
list_key =list(dict_x_y.items())
count = 0

list_key.sort(key = lambda i:i[1])
dict_start_finish = dict(list_key)
dict_finish_start = dict(reversed(list_key))
print('Начальный словарь: {name} '.format(name = dict_x_y))
print(f"Отсортирован по позрастанию значений: {dict_start_finish}")
print(f"Отсортирован по убыванию значений: {dict_finish_start}")
