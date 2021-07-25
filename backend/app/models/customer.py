from datetime import datetime
from typing import Optional

from app.models.core import CoreModel, IDModelMixin


class CustomerBase(CoreModel):
    first_name: Optional[str]
    last_name: Optional[str]
    email: Optional[str]
    created: Optional[datetime]
    modified: Optional[datetime]


class CustomerCreate(CustomerBase):
    first_name: str
    last_name: str
    email: str


class CustomerUpdate(CustomerBase):
    first_name: str
    last_name: str
    email: str


class CustomerInDB(IDModelMixin, CustomerBase):
    first_name: str
    last_name: str
    email: str


class CustomerPublic(IDModelMixin, CustomerBase):
    pass
