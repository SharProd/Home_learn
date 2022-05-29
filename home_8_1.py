""" Написать функцию create_frame, которая cоздаст рамку для переданной строки.
frame(['Create', 'a', 'frame'], '+') ->

++++++++++
+ Create +
+ a      +
+ frame  +
++++++++++"""


def frame(string:str)->str:
    split_string_list = list(i for i in  string.split(' ') if i!='')
    print(split_string_list)

    max_string_value = len(max(split_string_list,key=lambda x:len(x)))
    print(max_string_value)
    text_print = f'++{max_string_value*"+"}++\n'
    for item in split_string_list:
        x = max_string_value
        text_print+=f'+ {item:<{x}} +\n'
    text_print+= f'++{max_string_value*"+"}++'
    print(text_print)


frame('create a frame')