from .base import BaseSchema

class Resource2(BaseSchema):
    attr: int

class CreateResource2Request(BaseSchema):
    attr: int

class CreateResource2Response(BaseSchema):
    data: Resource2