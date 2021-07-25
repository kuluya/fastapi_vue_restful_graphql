from typing import List

from app.db.repositories.base import BaseRepository
from app.models.customer import CustomerCreate, CustomerInDB, CustomerUpdate

from fastapi import HTTPException
from starlette.status import HTTP_400_BAD_REQUEST


CREATE_CUSTOMER_QUERY = """
    INSERT INTO customers (first_name, last_name, email)
    VALUES (:first_name, :last_name, :email)
    RETURNING id, first_name, last_name, email, created, modified;
"""

GET_CUSTOMER_BY_ID = """
    SELECT id, first_name, last_name, email, created, modified
    FROM customers
    WHERE id = :id;
"""

GET_ALL_CUSTOMERS_QUERY = """
    SELECT id, first_name, last_name, email, created, modified
    FROM customers;
"""

UPDATE_CUSTOMER_QUERY = """
    UPDATE customers
    SET
        first_name = :first_name,
        last_name = :last_name,
        email = :email
    WHERE id = :id
    RETURNING id, first_name, last_name, email;
"""

DELETE_CUSTOMER_QUERY = '''
    DELETE FROM customers
    WHERE id = :id
    RETURNING id;
'''


class CustomersRepository(BaseRepository):
    async def create_customer(self, *, new_customer: CustomerCreate) -> CustomerInDB:
        values = new_customer.dict(exclude_none=True)
        customer = await self.db.fetch_one(query=CREATE_CUSTOMER_QUERY, values=values)

        return CustomerInDB(**customer)

    async def get_customer_by_id(self, *, id: int) -> CustomerInDB:
        customer = await self.db.fetch_one(query=GET_CUSTOMER_BY_ID, values={'id': id})

        return CustomerInDB(**customer) if customer else None

    async def get_all_customers(self) -> List[CustomerInDB]:
        customers = await self.db.fetch_all(query=GET_ALL_CUSTOMERS_QUERY)

        return [CustomerInDB(**customer) for customer in customers]

    async def update_customer(self, *, id, customer_update: CustomerUpdate) -> CustomerInDB:
        customer = await self.get_customer_by_id(id=id)

        if not customer:
            return None

        update_values = customer.copy(
            update=customer_update.dict(exclude={'created', 'modified'}),
            exclude={'created', 'modified'}
        )
        print(update_values)

        try:
            updated_customer = await self.db.fetch_one(
                query=UPDATE_CUSTOMER_QUERY,
                values=update_values.dict()
            )

            return CustomerInDB(**updated_customer)
        except Exception as e:
            print(e)
            raise HTTPException(
                status_code=HTTP_400_BAD_REQUEST,
                detail='Invalid Update values.'
            )

    async def delete_customer(self, *, id) -> int:
        customer = await self.get_customer_by_id(id=id)

        if not customer:
            return None
        deleted_id = await self.db.execute(query=DELETE_CUSTOMER_QUERY, values={'id': id})

        return deleted_id
