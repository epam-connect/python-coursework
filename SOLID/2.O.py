# Open & Closed principals
# Software entities(classes, functions) should be open for extension, not modification

class Animal:
    def __init__(self, name):
        self.name = name
    
    def get_name(self):
        pass


animals = [ Animal("lion"), Animal("mouse")]

def animal_make_sound(animals: list):       # function is not closed to new types of Animals
    for animal in animals:
        if animal.name == "lion":
            print("roar")
        elif animal.name == "mouse":
            print("squek")


animal_make_sound(animals)


class Lion(Animal):
    def make_sound(self):
        print("roar")

class Mouse(Animal):
    def make_sound(self):
        print("squek")

animals = [ Lion("lion"), Mouse('mouse')]

def animal_make_sound(animals: list):       # noew animal_make_sound is closed for any kind of animal
    for animal in animals:
        animal.make_sound()

animal_make_sound(animals)

