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


class ArticleBase(BaseModel):
    title: str
    body: Optional[str]


class ArticleCreate(ArticleBase):
    author: User


class Article(ArticleBase):
    id: int
    author_id: int

    class Config:
        orm_mode = True


class CommentBase(BaseModel):
    title: str
    body: Optional[str]


class CommentCreate(CommentBase):
    author: User


class Comment(CommentBase):
    id: int
    author_id: int

    class Config:
        orm_mode = True
