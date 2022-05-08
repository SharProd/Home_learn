#решить квадратное уравнение

print('''Решим квадратное уравнение типа ax**2+bx+c = 0
Подставьте значения a,d,c и узнаете чему равен  X .''')

print('#'*20)

a = float(input(' write number A:  '))
while a == 0:
        print("A не должно равняться нулю!!!")
        a = float(input(' write number A:  '))
b = float(input(' write number B:  '))
c = float(input(' write number C:  '))


D = b**2 - 4*a*c

if D>0:
    x_1 = float((-b + (D**0.5))/2*a)
    x_2 = float((-b - (D ** 0.5)) / 2*a)
    print(f'D>0  -  два корня\nx_1 = {round(x_1,1)}\nх_2 = {round(x_2,1)}')

if D==0:
    x = float(-b/(2*a))
    print(f'D = 0  -  один корень\nx = {round(x,1)}')

if D<0:
    print('D<0 , корнеей нет!')

