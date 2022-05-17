"""У вас есть массив чисел, составьте из них максимальное число. Например:  [61, 228, 9] -> 961228 """
number = input('Введите числа через запятую : ')
number_arr = number.split(',')
number_arr.sort(key = lambda i:i[0],reverse=True)
max_string_number = ''.join(number_arr)


print(max_string_number)

