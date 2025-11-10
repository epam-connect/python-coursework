from abc import ABC, abstractmethod

class Pizza(ABC):
    @abstractmethod
    def bake(self):
        pass

class ChickenPizza(Pizza):
    
    def bake(self):
        print("Cooking chicken pizza")


obj = ChickenPizza()
obj.bake()