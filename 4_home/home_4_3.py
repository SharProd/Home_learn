#На основании предоставленного отрывка текста определить 3_home наиболее часто встречаемых символа в ней.
#Пробелы нужно игнорировать (не учитывать при подсчете).
#Итог работы функции представить в виде словаря: {символ: количество раз, символ: количество раз, ... }.

from copy import deepcopy

string = 'aaaaaa bbbbb cccc ddd ee f'
list_string = list(i for i in string if i!=' ')
count_item_in_string = [list_string.count(i) for i in list_string]
count_copy = count_item_in_string
dict_max_item_in_string = dict(zip(list_string,count_item_in_string))
dict_max_item_in_string_copy = deepcopy(dict_max_item_in_string)

count = 1
while len(dict_max_item_in_string_copy.keys())>=4:
    for i in dict_max_item_in_string.keys():
        if dict_max_item_in_string[i]==count:
           dict_max_item_in_string_copy.pop(i)
        else:
            pass
    count+=1

print(dict_max_item_in_string_copy)


