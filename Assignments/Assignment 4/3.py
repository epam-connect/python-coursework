#Create class method, static method and instance method in a class

class MyClass:
    val = 10

    def instance_method(self):
        print("Works on instance")

    @classmethod
    def class_method(cls):          #cls (current class) is passed automatically
        print(f"class method, class veriable : {cls.val}")       # has access to class veriables
    
    @staticmethod
    def static_method():            #utility function
        print("static method")      #no access to class veriables
    

obj = MyClass()

obj.instance_method()
MyClass.class_method()
MyClass.static_method()