""" Напишите функции, которые покажут разницу в скорости проведения операций вставки,
 чтения, удаления между сетом и листом.
 Время выполнения производить с помощью декоратора и модуля datetime. """


from datetime import datetime

lisT = [i for i in range(1000)]
seT = {i for i in range(1000)}

def time_out(func):
    def time_result(*args,**kwargs):
        start = datetime.now()
        func(*args,**kwargs)
        result_time = datetime.now()-start
        print(result_time,end='  ')
        print(func.__annotations__['return'])
    return time_result


@time_out
def list_append(x:list)->list:
    x.append([i for i in range(1000,2001)] )
    print('update')
    return x


@time_out
def set_add(x:set)->set:
    x.update(i for i in range(1000,2001))
    print('update')
    return x


@time_out
def read_list(x:list)->list:
    print('read')
    for i in x:
        print(i, end='')
    print()


@time_out
def read_set(x: set) -> set:
    print('read')
    for i in x:
        print(i, end='')
    print()

@time_out
def clear_list(x:list)->list:
    x.clear()
    print('clear')
    return x


@time_out
def clear_set(x:set)->set:
    print("clear")
    x.clear()
    return x

list_append(lisT)
set_add(seT)
read_list(lisT)
read_set(seT)
clear_list(lisT)
clear_set(seT)