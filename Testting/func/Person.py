class Person:
    def __init__(self, name, age, credit):
        self.name = name
        self.age = age
        self.credit = credit
    
    def getCredit(self):
        return self.credit
    
    def setCredit(self, credit):
        self.credit = credit
    
    def getAge(self):
        return self.age
    
    def getName(self):
        return self.name
    
    # def __str__(self):
    #     return f"{self.name}, {self.age}, {self.credit}"


def is_eligable(person):
    return person.getAge() >= 18