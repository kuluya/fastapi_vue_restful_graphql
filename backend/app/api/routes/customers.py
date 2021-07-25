from typing import List

from fastapi import APIRouter, Body, Depends, HTTPException, Path
from starlette.status import HTTP_201_CREATED, HTTP_404_NOT_FOUND

from app.models.customer import CustomerPublic, CustomerCreate, CustomerUpdate
from app.db.repositories.customers import CustomersRepository
from app.api.dependencies.database import get_repository

router = APIRouter()


@router.get("/",
            response_model=List[CustomerPublic],
            name='customers:get-all-customers')
async def get_all_customers(
        customers_repo: CustomersRepository = Depends(get_repository(CustomersRepository))
) -> List[CustomerPublic]:
    return await customers_repo.get_all_customers()


@router.get("/{id}",
            response_model=CustomerPublic,
            name='customers:get-all-customers')
async def get_customers_by_id(
        id: int,
        customers_repo: CustomersRepository = Depends(get_repository(CustomersRepository))
) -> List[CustomerPublic]:
    return await customers_repo.get_customer_by_id(id=id)


@router.post('/',
             response_model=CustomerPublic,
             name='customers:create-customer',
             status_code=HTTP_201_CREATED)
async def create_customer(
        new_customer: CustomerCreate = Body(..., embed=True),
        customers_repo: CustomersRepository = Depends(get_repository(CustomersRepository))
) -> CustomerPublic:
    created_customer = await customers_repo.create_customer(new_customer=new_customer)
    return created_customer


@router.put('/{id}',
            response_model=CustomerPublic,
            name='customers:update-customer')
async def update_customer(
        id: int = Path(..., ge=1, title='The ID of the customer to update.'),
        customer_update: CustomerUpdate = Body(..., embed=True),
        customers_repo: CustomersRepository = Depends(get_repository(CustomersRepository))
) -> CustomerPublic:
    updated_customer = await customers_repo.update_customer(
        id=id,
        customer_update=customer_update,
    )

    if not updated_customer:
        raise HTTPException(
            status_code=HTTP_404_NOT_FOUND,
            deteil='No customer found with that id.'
        )

    return updated_customer


@router.delete('/{id}', response_model=int, name='customer:delete-customer')
async def delete_customer(
        id: int = Path(..., ge=1, title='The ID of the customer to delete.'),
        customer_repo: CustomersRepository = Depends(get_repository(CustomersRepository))
) -> int:
    deleted_id = await customer_repo.delete_customer(id=id)

    if not deleted_id:
        raise HTTPException(
            status_code=HTTP_404_NOT_FOUND,
            detail='No customer found with that id.')

    return deleted_id
