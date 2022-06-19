class Human:
    __country = "USSR"
    def __init__(self,name,age,weight,height):
        self.name = name
        self.age = age
        self. weight = weight
        self.height = height

    def __str__(self):
        string = f"""
    name - {self.name}
    age - {self.age}
    weight - {self.weight}
    height - {self.height}"""
        return string

    def __add__(self, other):
        string = f"it is family, {self.name}+{other.name}"
        return  string

    def __eq__(self, other):
        if self.age == other.age:
            return  "yes"
        elif self.age > other.age:
            return f"{self.name} more years than {other.name}"
        else:
            return f"{other.name} more years than {self.name}"


class Kid(Human):
    def __init__(self, birth_weight, mother, father,name,age,weight,height):
        super().__init__(name,age,weight,height)
        self.birth_weight = birth_weight
        self. mother = mother
        self.father = father

    def __str__(self):
        string = f"""
    name - {self.name} 
    birth weight - {self.birth_weight}
    mother - {self.mother}
    father - {self.father}"""
        return  string

class Teenager(Human):
    def __init__(self,school_class,name,age,weight,height):
        super().__init__(name,age,weight,height)
        self.school_class = school_class


class Worker(Teenager):
    def __init__(self,work_experience,post,salary,school_class,name,age,weight,height):
        super().__init__(school_class,name,age,weight,height)
        self.work_experience = work_experience
        self.post = post
        self. salary = salary


class Doctor(Worker):
    def __init__(self,work_experience,post,salary,school_class,name,age,weight,height,training_time):
        super().__init__(work_experience,post,salary,school_class,name,age,weight,height)
        self.training_time = training_time



jack = Human('Jack',58,80,182)
print(jack)


mikki = Kid(3200,'Jessi','Fred','Mikki',2,5,50)
print(mikki)

print(jack+mikki)
print(jack==mikki)
print(Doctor.mro())

print(Human._Human__country)



