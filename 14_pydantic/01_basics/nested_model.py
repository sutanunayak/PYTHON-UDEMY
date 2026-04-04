from typing import List, Optional
from pydantic import BaseModel


class Address(BaseModel):
    street: str
    city: str
    zip_code: str

class User(BaseModel):
    id: int
    name: str
    address: Address

address = Address(
    street="123 something",
    city="Dhenkanal",
    zip_code="751001"
)

user = User(
    id=1,
    name="Sutanu",
    address=address,
)


user_data = {
    "id": 1,
    "name": "Sutanu",
    "address": {
        "street": "345 something",
        "city": "cuttack",
        "zip_code": "754001"
    }
}


user = User(**user_data)
print(user)