from app.db.repositories.base import BaseRepository
from app.models.customer import CustomerCreate, CustomerInDB


CREATE_CUSTOMER_QUERY = """
    INSERT INTO customers (first_name, last_name, email, created, modified)
    VALUES (:first_name, :last_name, :email, :created, :modified)
    RETURNING id, first_name, last_name, email, created, modified;
"""


class CustomersRepository(BaseRepository):
    async def create_customer(self, *, new_customer: CustomerCreate) -> CustomerInDB:
        values = new_customer.dict()
        customer = await self.db.fetch_one(query=CREATE_CUSTOMER_QUERY, values=values)

        return customer
