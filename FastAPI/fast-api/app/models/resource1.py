from app.schemas.resource1 import Resource1

async def create(attr: int):
    return Resource1(attr=attr)