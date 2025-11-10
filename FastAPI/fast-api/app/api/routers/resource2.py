from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.common.db import get_session
from app.schemas.resource2 import CreateResource2Response, CreateResource2Request, Resource2
from app.models import resource2



router = APIRouter(prefix='/resource2')

@router.get('')
async def get_resource2():
    return ''

@router.post('')
async def create_resource2(
        create_req: CreateResource2Request,
        session: AsyncSession =  Depends(get_session)
) -> CreateResource2Response:
    data = await resource2.create(session=session, **create_req.model_dump())
    return CreateResource2Response(data=data)

