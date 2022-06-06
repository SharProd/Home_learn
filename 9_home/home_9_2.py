"""Написать функцию для подсчета количества строк, слов и букв в текстовом файле."""

def counter(file_read:str)->str:
    with open(file_read,'r') as file:
        txt = file.readlines()
        count_line = len(txt)
        count_letter = sum(list(map(lambda x:len(x),txt)))

    with open(file_read,'r') as file:
        txt_2 = file.read()

        count_word = len(txt_2.split(' '))
        print(txt_2.split(' '))

    print(f"""
    line - {count_line}
    word - {count_word}
    letter - {count_letter}""")



counter('article_2.txt')