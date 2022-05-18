"""Написать программу, принимающую 1 аргумент — число от 0 до 1000, и возвращающую True,
 если оно простое, и False - иначе"""
x = int(input('write number: '))
y = int(x)/2 +1
result = ''
for i in range(2,int(y)):
    if x%i==0:
        result = 'не простое'
        break
    else:
        result = 'простое'
print(result)
