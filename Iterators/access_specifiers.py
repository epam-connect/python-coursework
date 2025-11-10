class myclass:
    a = 10
    def __init__(self, name, age, salary, number):
        self.name = name        # public
        self._age = age         #protected
        self.__salary = salary  #private
        self.__number__ = number  
    
    
    def get(self):
        return self.a
    

obj = myclass("Ankan", 22, 20000, 8155215252)
print(obj._age)
# print(obj.__salary) #error
print(obj._myclass__salary) # this words for private veriables called class mangling
print(obj.__number__)
# obj = myclass()
# obj2 = myclass()

# obj.a -= 1
# print(obj.a, obj2.a)