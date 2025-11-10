from .base import BaseSchema

class Resource1(BaseSchema):
    attr: int

class CreateResource1Request(BaseSchema):
    attr: int

class CreateResource1Response(BaseSchema):
    data: Resource1


