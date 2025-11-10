from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.common.db import get_session
from app.schemas.resource1 import CreateResource1Response, CreateResource1Request
from app.models import resource1

router = APIRouter(prefix='/resource1')

@router.get('')
async def get_resource1():
    from app.common.settings import settings
    print(settings.DB_URL)
    return ''

@router.post('')
async def create_resource1(
        create_req: CreateResource1Request,
        session: AsyncSession = (Depends(get_session))
) -> CreateResource1Response:
    new_resource = await resource1.create(**create_req.model_dump())
    return CreateResource1Response(data=new_resource)

