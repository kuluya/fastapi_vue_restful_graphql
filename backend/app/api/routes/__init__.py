from fastapi import APIRouter
from app.api.routes.hogehoge import router as hogehoge_router


router = APIRouter()
router.include_router(hogehoge_router, prefix="/hogehoge", tags=["hogehoge"])
