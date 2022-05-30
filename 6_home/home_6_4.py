""" Написать программу, которая посчитает кол-во одинаковых элементов в списке.
 Список будет заполняться рандомными целыми числами.
 Рекомендую использовать несколько функций
 (для заполнения списка целыми числами, для подсчета количества, для вывода)"""
from random import random

def edit_list(len_list:int)->list:
    x_list = []
    for i in range(len_list):
        x_list.append(int(random()*100))
    return  x_list

def count_list_number(lisT:list)->dict:
    counter=dict()
    for i in lisT:
       if lisT.count(i)>1:
           counter[i]=lisT.count(i)
    return counter

def show(dicT:dict)->str:
    text = f'повторяющееся элементы:\n'
    if len(dicT)>0:
        for i in dicT.keys():
            text+=f'{i} - количество {dicT[i]} \n'
    else:
        text = ' нет повторяющихся элементов'
    return text

print(show(count_list_number(edit_list(100))))
print(edit_list.__annotations__)
print(count_list_number.__annotations__)
print(show.__annotations__)