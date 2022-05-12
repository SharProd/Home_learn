# Первые n чисел последовательности Фибоначчи.
count = int(input('Сколько чисел в последовательности вы хотите увидеть? - '))
fib_list =[1,1]

for i in range(2,count):
    fib_list.append(fib_list[-2]+fib_list[-1])

for num in fib_list:
    print(num, end= ' ')
