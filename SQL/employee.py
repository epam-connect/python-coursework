class Employee:
    def __init__(self, first, last, salary):
        self.first = first
        self.last = last
        self.salary = salary
    
    @property
    def email(self):
        return f"{self.first}{self.last}@gmail.com"

    def __repr__(self):
        return f"Employee({self.first, self.last, self.salary})"
        