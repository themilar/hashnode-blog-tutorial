from http.client import HTTPException
from sqlalchemy.orm import Session
import hashlib
from . import models, schemas

hash = hashlib.sha256()


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    hash.update(user.password.encode("utf-8"))
    hashed_password = hash.hexdigest()

    db_user = models.User(email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Item).offset(skip).limit(limit).all()


def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
    db_item = models.Item(**item.dict(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def get_articles(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Article).offset(skip).limit(limit).all()


def create_article(db: Session, article: schemas.ArticleCreate, user_id: int):
    db_item = models.Article(**article.dict(), author_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def get_object_or_404(db: Session, Model: models.Base, object_id: int):
    db_item = db.query(Model).filter(Model.id == object_id).first()
    if db_item is None:
        raise HTTPException(status=404, detail="Not found")
    return db_item

    # db_item = (
    #     db.query(getattr(models, f"{Model}"))
    #     .filter(getattr(models, f"{Model}").id == object_id)
    #     .first()
    # )
