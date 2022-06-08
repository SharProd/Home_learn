
class Car:
    def __init__(self,color,type_car,year):
        self.color = color
        self.type_car = type_car
        self.year = year

    def __str__(self):
        string = f"""{self.__dict__}"""
        return string

    def start_engine(self):
        return 'Engine is start'

    def stop_engine(self):
        return 'Engine is stop'

    def year_car(self,year):
        self.year = year
        return self.year

    def car_type(self,type_car):
        self.type_car = type_car
        return self.type_car

    def car_color(self,color):
        self.color = color
        return self.color

jeely = Car('red','racing',1994)
print(jeely)
print(jeely.start_engine())
print(jeely.stop_engine())
jeely.car_color('white')
jeely.car_type('truck')
jeely.year_car(2015)
print(jeely)