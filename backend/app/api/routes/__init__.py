from fastapi import APIRouter
from app.api.routes.customers import router as customer_router


router = APIRouter()
router.include_router(customer_router, prefix="/customer", tags=["customer"])
