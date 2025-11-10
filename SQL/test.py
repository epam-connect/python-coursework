class MyClass:
    def __init__(self):
        self.__x = 10


class ChildClass(MyClass):
    def __init__(self):
        super().__init__()
        self.x = self._MyClass__x
    
    def get(self):
        return self.x
    

# print(ChildClass().get())
a = "[('Inception', 5, 'Mind-blowing!'), ('Interstellar', 4, 'Great visuals but complex plot'), ('Interstellar', 4, 'Great visuals but complex plot')]"
a = a.replace(" ","")
a = a.strip("[]()")
# print(a)
# a = a.replace("),(", "|")
a = a.split("),(")

reviews = []

for item in a:
    item = item.strip("''")
    # print(item)
    reviews.append(tuple(item.split("','")))


print(reviews)
# for item in a:
#     print(item)
# a = [ tuple(item.strip('()').split(',')) for item in a]
# print(a)