""" Напишите функцию sum_range(start, end),
которая суммирует все целые числа от значения «start» до величины «end» включительно.
Если пользователь задаст первое число большее чем второе, просто поменяйте их местами. """

def sum_start_end(x:int,y:int)->int:
    if x>y:
        x,y = y,x
    z = sum([ i for i in range(x,y+1)])
    return z


print(sum_start_end(2,4))
print(sum_start_end.__annotations__)