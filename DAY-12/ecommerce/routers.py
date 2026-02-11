from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
import models
import schemas

auth_router = APIRouter()
product_router = APIRouter()
blog_router = APIRouter()
comment_router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Auth
@auth_router.post("/register")
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    new_user = models.User(username=user.username, email=user.email, hashed_password=user.password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

# Products
@product_router.post("/")
def add_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    new_product = models.Product(**product.dict())
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product

@product_router.get("/")
def list_products(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(models.Product).offset(skip).limit(limit).all()

# Blogs
@blog_router.post("/")
def create_blog(blog: schemas.BlogCreate, db: Session = Depends(get_db)):
    new_blog = models.Blog(**blog.dict())
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

@blog_router.post("/{blog_id}/like")
def like_blog(blog_id: int, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).get(blog_id)
    blog.likes += 1
    db.commit()
    return {"likes": blog.likes}

# Comments
@comment_router.post("/")
def add_comment(comment: schemas.CommentCreate, db: Session = Depends(get_db)):
    new_comment = models.Comment(**comment.dict())
    db.add(new_comment)
    db.commit()
    db.refresh(new_comment)
    return new_comment