"""Написать рекурсивную функцию, которая осуществляет суммирование чисел во входящем списке."""


def sum_list(x:list,y:float=0)->float:
    if len(x)<=1:
        y+=x[0]
        return y
    else:
        y+=x[0]
        return sum_list(x[1:],y)
print(sum_list([2,3,4,1,-20]))

print(sum_list.__annotations__)