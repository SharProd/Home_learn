"""Написать рекурсивную функцию, которая осуществляет суммирование чисел во входящем списке."""


def sum_list(x,y=0):
    if len(x)<=1:
        y+=x[0]
        return y
    else:
        y+=x[0]
        return sum_list(x[1:],y)
print(sum_list([2,3,4,1,-20]))