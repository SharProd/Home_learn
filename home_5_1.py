"""Написать программу, принимающую 1 аргумент — число от 0 до 1000, и возвращающую True,
 если оно простое, и False - иначе"""
x = int(input('write number: '))
list_y = [1,2,3,4,5,6,7,8,9]
bool_check = 0
for i in list_y:
    if x%i==0:
        bool_check+=1
if bool_check>2:
    print('не простое')
else:
    print('Простое')