"""Напишите функцию, которая примет в кач-ве аргумента integer (секунды)
и вернет итоговое время в формате HH:MM:SS.
Например: (seconds=3666) -> 01:01:06"""
import time


# def str_time(time:int)->str:
#     hours = 0
#     minute = 0
#     second = 0
#     while time>59:
#         time-=60
#         minute+=1
#         if minute>59:
#             hours+=1
#             minute=0
#
#     return f'{hours:0>2}:{minute:0>2}:{time:0>2}'
#
# print(str_time(3666))


def str_time(s:int)->str:
    t = time.strftime('%H:%M:%S',time.gmtime(s))
    return t

print(str_time(3666))