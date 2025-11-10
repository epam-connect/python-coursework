# S : Single Responsibility
# Each software component eg. class, functions should have a single responsibility

class Animal:
    def __init__(self, name):
        self.name = name
    
    def get_name(self):             # Animal properties management
        pass
    
    def save(self, animal):         # Animal database management function, violates SRP
        pass


class Animal:                       # manages only Animal management properties
    def __init__(self, name):
        self.name = name
    
    def get_name(self) -> str:
        pass

class AnimalDB:
    def save(self, animal : Animal):    # seperating all Animal db operations in AnimalDB class
        pass    
    
    def get_animal(self, id):
        pass


'''
Down side here is that client of Animal class will have to manage two classes
We can apply facade pattern. Animal class acts as facade for AnimalDB class
'''

class Animal:
    def __init__(self, name):
        self.name = name
        self.db = AnimalDB()

    def get_name(self) -> str:
        pass

    def get_animal(self, id):
        return self.db.get_animal(id)

    def save(self):
        self.db.save(animal=self)

    