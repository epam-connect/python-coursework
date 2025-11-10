from typing import final

class Parent:
    @final
    def show(self):
        print("This method cannot be overridden")

class Child(Parent):
    def show(self):  # ❌ mypy error: Cannot override a final method
        print("Overridden method")

a = Child()
a.show()

