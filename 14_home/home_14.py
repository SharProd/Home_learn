# Домашнее задание на четверг:
# 1. Cоздать 2 класса: Human (атрибуты: male, age, account(кол-во денег на счету), метод: предоставить информацию о себе). House(атрибуты: price, square. методы: предоставить скидку).
# Реализовать функцию (или несколько функций), которая проанализирует существующие дома и подберет лучший вариант для определенного человека. По каким критериям будет выбираться лучший вариант, выберите самостоятельно)

class Human():
    def __init__(self,male, age, account):
        self.male = male
        self.age = age
        self.account = account

    def __str__(self):
        return f"{self.male} {self.age} {self.account}"

    def info(self)->str:
        male = f'male - {self.male}'
        age = f'age - {self.age}'
        account = f'account - {self.account}'
        return f"""
    {male}
    {age}
    {account}
"""

class House():
    def __init__(self,price, square,adress):
        self.price = price
        self.square = square
        self.adress = adress

    def __str__(self):
        return f'{self.price}  {self.square} {self.adress}'

    def sale(self,sale:float)->str:
        self.price -= self.price*sale//100
        return f'''
    price - {self.price}
    sale {sale}
'''

def buy_house(human,*houses):

    house = ""
    if human.account < 30000:
        price = min(map(lambda x: x.price, houses))
        adress = [i.adress for i in houses if i.price == price]
        adress = adress[0]
    else:
        price = max(map(lambda x: x.price, houses))
        adress = [i.adress for i in houses if i.price == price]
        adress = adress[0]
    house = f'adress {adress} price - {price}'
    print(house)




# house = House(10000,300,"12/23/23")
# house2 = House(12999,432,'we3/23/23.2')
# house3 = House(90000,530,'df/23/cc/2')
# human = Human('man',25,333344)
# human2 = Human('woman',60,10000)
# human3 = Human('man',45,122000)
# print(human.info())
# print(house)
# print(house.sale(15.5))
# print()
# buy_house(human,house,house3,house2)