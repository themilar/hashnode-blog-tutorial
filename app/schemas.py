import email
from typing import List, Optional

from pydantic import BaseModel, EmailStr


class ItemBase(BaseModel):
    title: str
    description: Optional[str] = None


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: EmailStr


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    items: List[Item] = []

    class Config:
        orm_mode = True
        schema_extra = {
            "sample": {
                "is_active": True,
                "email": "testuser@api.com",
                "id": 4,
                "items": ["apple", "oranges"],
            }
        }
