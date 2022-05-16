"""Есть число n, возьмите сумму цифр n.
Если это значение имеет более одной цифры, продолжайте уменьшать таким образом,
пока не будет получено однозначное число. Ввод будет неотрицательным целым числом.
Пример:
16  -->  1 + 6 = 7
942  -->  9 + 4 + 2 = 15  -->  1 + 5 = 6
132189  -->  1 + 3 + 2 + 1 + 8 + 9 = 24  -->  2 + 4 = 6
493193  -->  4 + 9 + 3 + 1 + 9 + 3 = 29  -->  2 + 9 = 11  -->  1 + 1 = 2"""

def sum_number(string):
    string = str(string)
    string_sum = 0
    if len(string)>1:
        for i in string:
            string_sum += int(i)
        return sum_number(string_sum)
    else:
        return string

print(sum_number(int(input('write number : '))))