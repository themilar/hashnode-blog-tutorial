import email
from typing import List, Optional

from pydantic import BaseModel, EmailStr


class ArticleBase(BaseModel):
    title: str
    body: Optional[str]


class ArticleCreate(ArticleBase):
    pass


class Article(ArticleBase):
    id: int
    author_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: EmailStr


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    articles: List[Article] = []

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
