#Create class that can count no. of instances created using the class

class MyClass:
    object_count = 0

    def __init__(self):
        print("Object created")
        MyClass.object_count += 1   # 1st method way

    # def __new__(cls):             # 2nd method
    #     cls.object_count += 1
    #     return super(MyClass, cls).__new__(cls)

    @classmethod
    def get_object_count(cls):
        return cls.object_count

for i in range(10):
    MyClass()

print(MyClass.get_object_count())