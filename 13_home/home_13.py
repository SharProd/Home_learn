from functools import reduce
from sys import getsizeof


def number_fuctorial_gen(n:int):
    fuct_n = reduce(lambda x,y:x*y,(i for i in range(1,n+1)))
    return fuct_n

def fub_number():
    a = 1
    b = 1
    for i in range(1000):
        yield a
        a,b=b,a+b

# for i in fub_number(100):
#     print(i, end = ' ')
print(getsizeof(fub_number))

# print(number_fuctorial_gen(20))