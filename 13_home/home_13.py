from functools import reduce
from sys import getsizeof


def number_fuctorial_gen(n:int):
    fuct_n = reduce(lambda x,y:x*y,(i for i in range(1,n+1)))
    return fuct_n

def fub_number():
    a = 1
    b = 1
    for i in range(100-2):
        yield a
        a,b=b,a+b


def fub_number_default():
    a = [1,1]
    while len(a)<100:
        x = a[-1]+a[-2]
        a.append(x)
    return  a

a = fub_number_default()
print(getsizeof(a))
# for i in fub_number(100):
#     print(i, end = ' ')
b = fub_number()
print(getsizeof(b))