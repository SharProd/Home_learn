import datetime
from datetime import date

class User:
    def __init__(self,name, surname, age, country, gender, profession):
        self.name = name
        self.surname = surname
        self.age = age
        self.country = country
        self.gender = gender
        self.profession = profession

    def __str__(self):
        string = self.__dict__
        return str(string)


    def email(self):
        self.email_adress = input('your email? : ')
        return self.email_adress

    def birth_year(self):
        year = datetime.date.year()
        return self.age-year

    def policeman():
        policeman = User('Pit','Pat',43,'Great Britan','Man','Policeman')
        return  policeman

    def teacher():
        teacher = User('Pit','Pat',43,'Great Britan','Man','Teacher')
        return teacher

    def doctor():
        doctor = User('Pit','Pat',43,'Great Britan','Man','Doctor')
        return doctor

jack = User('Jack','Spit',35,'China','Man','Driver')
print(jack)
print(User.doctor())
print(User.policeman())
print(User.teacher())
