"""Напишите функцию, которая принимает аргумент в виде списка из 12 элементов от 0-9 и возвращает этот список в виде номера телефона.
[1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 0, 4] -> +123(45)678-91-04"""
from random import randint


def phone_number_in_list(func:any)->str:
    def decor_func(*args,**kwargs):
        lisT = list(str(i) for i in (func(*args,**kwargs)))
        region = ''.join(lisT[0:3])
        code_operator = ''.join(lisT[3:5])
        phone_number = ''.join(lisT[5:])
        print(f'+{region}({code_operator}){phone_number}')
    return decor_func


@phone_number_in_list
def random_list_edit()->list:
    return list(randint(0,9) for i in range(12))

random_list_edit()


