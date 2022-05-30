""" Написать функцию create_frame, которая cоздаст рамку для переданной строки.
frame(['Create', 'a', 'frame'], '+') ->

++++++++++
+ Create +
+ a      +
+ frame  +
++++++++++"""


def frame(string:str,simbol:str)->str:
    split_string_list = list(i for i in  string.split(' ') if i!='')
    max_string_value = len(max(split_string_list,key=lambda x:len(x)))
    text_print = f'{simbol*2}{max_string_value*simbol}{simbol*2}\n'
    for item in split_string_list:
        x = max_string_value
        text_print+=f'{simbol} {item:<{x}} {simbol}\n'
    text_print+= f'{simbol*2}{max_string_value*simbol}{simbol*2}'
    return text_print


print(frame('create a frame home   work','#'))
print(frame.__annotations__)