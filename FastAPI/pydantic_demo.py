class ValidationError(Exception):...

class BaseValidator:
    def __init__(self, *args, **kwargs):
        for f_name, f_type in self.__annotations__.items():
            val = kwargs.get(f_name, None)
            if not isinstance(val, f_type):
                raise ValidationError

class Point(BaseValidator):
    x : int
    y : int

print(Point.__annotations__)

Point(x=10, y = "20")