from abc import ABC, abstractmethod

class AbstractClass(ABC):
    def fun(self):
        print("Hello from bastract class")
    
    @abstractmethod
    def abstract_fun(self):
        pass
    

class Child(AbstractClass):
    def abstract_fun(self):
        print("overridden abstract method")

obj = Child()
obj.abstract_fun()