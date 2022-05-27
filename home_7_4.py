'''Напишите программу которая настроит отображение комментария к отметке 'мне нравится'
в условном посте. Список имен передается в кач-ве аргумента.
Например:
[]                                -->  "no one likes this"
["Peter"]                         -->  "Peter likes this"
["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"'''

def like_this(lisT:list)->str:
    if len(lisT)==0:
        print("no one likes this")
    elif len(lisT)==1:
        print(f"{lisT[0]} likes this")
    elif len(lisT)==2:
        print(f'{lisT[0]}, {lisT[1]} like this')
    elif len(lisT)==3:
        print(f'{lisT[0]}, {lisT[1]} and {lisT[2]} others like this')
    elif len(lisT)>3:
        print(f'{lisT[0]}, {lisT[1]} and {len(lisT[2:])} others like this')

like_this(["Alex", "Jacob", "Mark",'Max'])