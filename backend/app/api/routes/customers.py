from typing import List

from fastapi import APIRouter, Body, Depends
from starlette.status import HTTP_201_CREATED

from app.models.customer import CustomerPublic, CustomerCreate
from app.db.repositories.customers import CustomersRepository
from app.api.dependencies.database import get_repository

router = APIRouter()


@router.get("/")
async def get_all_customers() -> List[dict]:
    customers = [
        {'id': 1, 'first_name': '大和', 'last_name': '大和', 'email': 'yamato@example.com', 'created': '1940-08-08',
         'modified': '2021-07-23'},
        {'id': 2, 'first_name': '長門', 'last_name': '大和', 'email': 'yamato@example.com', 'created': '1919-11-09',
         'modified': '2021-07-23'},
    ]

    return customers


@router.post('/',
             response_model=CustomerPublic,
             name='customers:create-customer',
             status_code=HTTP_201_CREATED)
async def create_customer(
        new_customer: CustomerCreate = Body(..., embed=True),
        customers_repo: CustomersRepository = Depends(get_repository(CustomersRepository)),
) -> CustomerPublic:
    created_customer = await customers_repo.create_customer(new_customer=new_customer)
    return created_customer
