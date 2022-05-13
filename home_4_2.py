#Создайте словарь с количеством элементов не менее 5-ти.
# Поменяйте местами первый и последний элемент объекта.
# Удалите второй элемент. Добавьте в конец ключ «new_key» со значением «new_value».
# Выведите на печать итоговый словарь. Важно, чтобы словарь остался тем же (имел тот же адрес в памяти).

#Словарь - это не упорядоченый тип данных, здесь деля выбрать второй или еще какой нибудь элемент,
#Выбор идет по ключу или значению.

dict_person = {'name' : 'Ivan' ,
               'surname' : 'Ivanov' ,
               'nikname' : 'Vania93' ,
               'age' : 29 ,
               'phone_number' : '+8567842369' }


print('Start dictionary: \n ', dict_person,'\n','id [dict_person] :', id(dict_person))
dict_person['new_key'] = 'new_value'
dict_person.pop('surname')
print('Start dictionary: \n ', dict_person,'\n','id [dict_person] :', id(dict_person))
