"""Документ «article.txt» содержит произвольный текст.
Требуется реализовать функцию longest_words(file),
которая выводит слово, имеющее максимальную длину (или список слов, если таковых несколько)."""


def longest_words(file_read:str)->str:
    with open(file_read,'r') as file:
        text = file.read()
        count = sorted(text.split(' '),key= len, reverse=True)
        longest_words_list = [ i for i in count[1:] if len(i)==len(count[0])]
        longest_words_list.append(count[0])
        print(longest_words_list[0]) if len(longest_words_list)==1 else print(longest_words_list)
        print(text.isspace())
        print(text)
longest_words('article_2.txt')