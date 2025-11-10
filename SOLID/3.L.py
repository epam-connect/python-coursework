
'''
Liskov Substitution Principle

A sub-class must be substitutable for its super-class.  The aim of this
principle is to ascertain that a sub-class can assume the place of its
super-class without errors.  If the code finds itself checking the type of class
then, it must have violated this principle.

* By following LSP,  we naturally make our code OCP-compliant, avoiding changes in existing code

Let’s use our Animal example.

'''


class Animal:
    def __init__(self, name=""):
        self.name = name
    
    def get_name(self):
        pass


class Lion(Animal):
    def make_sound(self):
        print("roar")

class Mouse(Animal):
    def make_sound(self):
        print("squek")

animals = [Lion(), Mouse()]

def make_animals_sound(animals: list):
    for animal in animals:
        animal.make_sound()


make_animals_sound(animals)


