""" Напишите функцию, которая принимает два числа в кач-ве аргументов
и считает наименьшее общее кратное для этих чисел."""

def two_numbers(x:int,y:int):
    count = [i for i in range(2,x) if x%i==0 and y%i==0]
    if len(count)>0:
        print(min(count))
        print(count)
    else:
        print('кроме единицы общих кратных нет')

two_numbers(130,160)