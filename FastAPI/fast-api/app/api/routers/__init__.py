from fastapi import APIRouter

from .resource1 import router as r1_router
from .resource2 import router as r2_router

router = APIRouter(prefix="")

router.include_router(r1_router)
router.include_router(r2_router)
