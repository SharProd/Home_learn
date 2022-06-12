
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
        year_of_birth = date.today()
        return year_of_birth.year - self.age

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
#jack.email()
print(jack.birth_year())
print(jack)
print(User.doctor())
print(User.policeman())
print(User.teacher())
